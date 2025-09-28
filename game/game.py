import pygame as pg

from game.ecs.components.dash import Dash
from game.ecs.components.death import Death
from game.ecs.components.death import Death
from game.ecs.components.enemy import Enemy
from game.ecs.entity import Entity
from game.ecs.components.collider import Collider
from game.ecs.components.player import PlayerComponent
from game.ecs.components.person_sprite import PersonSprite
from game.ecs.components.physics import Movement, Position, Rotation, Velocity
from game.ecs.components.speed import Speed
from game.ecs.entitytypes.shoot import shoot
from game.ecs.systems.bullets import BulletSystem
from game.ecs.systems.bullet_collision import BulletCollisionSystem
from game.ecs.systems.dash import DashSystem
from game.ecs.systems.deaths import DeathSystem
from game.ecs.systems.enemy_ai_system import EnemyAISystem
from game.config.enemy_ai_config import ENEMY_SHOOT_COOLDOWN, ENEMY_SHOOT_RANGE
from game.ecs.systems.input import InputSystem
from game.ecs.systems.level_system import LevelSystem
from game.ecs.systems.hud_system import HUDSystem
from game.ecs.systems.movement import MovementSystem
from game.ecs.systems.render import RenderSystem
from game.ecs.systems.timer_system import TimerSystem
from game.ecs.systems.upgrades import UpgradeSystem
from game.ecs.systems.weapon_system import WeaponSystem
from game.sprites.sprite import Sprite
from game.background import load_game_background, create_game_overlay
from util.prepare import CLOCK, SURF
from util.screens import Screens
from util.update_screen import update_screen


async def game(level_system=None) -> tuple[Screens, object] | Screens:
	print("started game!")
	
	if level_system is None:
		level_system = LevelSystem()
	
	player = Entity()
	player.add_components(level_system.get_level_spawn(), Velocity(0, 0), Speed(500), PersonSprite(Sprite("player_bodies", "a")), PlayerComponent(), Collider(128, 128), Rotation(), Dash(800), Movement())
	input_system = InputSystem()
	movement_system = MovementSystem()
	dash_system = DashSystem()
	bullet_system = BulletSystem()
	bullet_collision_system = BulletCollisionSystem()
	death_system = DeathSystem()
	enemy_ai_system = EnemyAISystem()
	enemy_ai_system.configure(cooldown=ENEMY_SHOOT_COOLDOWN, range=ENEMY_SHOOT_RANGE)
	timer_system = TimerSystem()
	weapon_system = WeaponSystem()
	upgrade_system = UpgradeSystem()
	hud_system = HUDSystem()
	render_system = RenderSystem()
	
	background = load_game_background()
	overlay = create_game_overlay()

	entities = {player}
	entities.update(level_system.get_enemies())
	level_system.start_level(entities)
	
	while True:
		dt = CLOCK.tick(60) / 1000.0

		for event in pg.event.get():
			if event.type == pg.QUIT:
				raise SystemExit
			if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
				return Screens.INGAMEMENU, hud_system
			
			if event.type == pg.KEYDOWN and event.key == pg.K_TAB:
				weapon_system.switch_weapon(1)
			
			if (event.type == pg.KEYDOWN and event.key == pg.K_f) or (event.type == pg.MOUSEBUTTONDOWN and event.button == 1):
				weapon_system.start_firing(weapon_system.get_current_weapon())
			
			if (event.type == pg.KEYUP and event.key == pg.K_f) or (event.type == pg.MOUSEBUTTONUP and event.button == 1):
				weapon_system.stop_firing(weapon_system.get_current_weapon())

		dash_system.update(entities, dt)
		input_system.update(player)
		movement_system.update(entities, dt, level_system.level)
		enemy_ai_system.update(entities, player)

		wall_collision_bullets = bullet_collision_system.update(entities, level_system.level)
		entities.difference_update(wall_collision_bullets)
		
		new_deaths = bullet_system.update(entities, level_system.level)
		if player in new_deaths:
			if not player.has_component(Death):
				player.add_component(Death())
			player.get_component(Death).death = True
			player_pos = player.get_component(Position)
			player_pos.x, player_pos.y = level_system.get_level_spawn().x, level_system.get_level_spawn().y
			death_system.reset_entity_death(player)
		
		entities_to_remove = new_deaths - {player}
		entities.difference_update(entities_to_remove)
		upgrade_system.update(player)
		death_system.deaths.update(entities_to_remove)
		if player in new_deaths:
			death_system.deaths.add(player)
		
		remove = death_system.update()
		remove.discard(player)
		entities.difference_update(remove)
		render_system.blood_positions.update(map(lambda d: d.get_component(Position), filter(lambda e: e.has_component(Enemy), remove)))
		
		timer_remove = timer_system.update(entities, dt)
		entities.difference_update(timer_remove)
		
		level_system.update_player_count(entities)
		
		
		if level_system.check_level_complete():
			level_system.complete_level()
			if level_system.is_game_complete():
				return Screens.FINALSUMMARY, level_system
			else:
				return Screens.LEVELCLEAR, level_system
		
		current_weapon = weapon_system.get_current_weapon()
		if weapon_system.shoot(current_weapon):
			player_pos = player.get_component(Position)
			player_rotation = player.get_component(Rotation)
			entities.add(shoot(player_pos, player_rotation, player.id))

		SURF.blit(background, (0, 0))
		SURF.blit(overlay, (0, 0))

		render_system.update(entities, player, level_system.level, weapon_system)
		
		kill_count = player.get_component(PlayerComponent).kills
		hud_system.render(kill_count)
		level_system.update(entities)
		if level_system.check_level_complete():
			level_system.complete_level()
			if level_system.is_game_complete():
				return Screens.FINALSUMMARY, level_system
			else:
				return Screens.LEVELCLEAR, level_system

		await update_screen()