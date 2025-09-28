import pygame as pg

from game.ecs.components.dash import Dash
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
			# if event.type == pg.KEYDOWN and event.key == pg.K_i:
			# 	return Screens.GAMEOVER
			# if event.type == pg.KEYDOWN and event.key == pg.K_o:
			# 	return Screens.LEVELCLEAR
			
			if event.type == pg.KEYDOWN and event.key == pg.K_TAB:
				weapon_system.switch_weapon(1)
			
			if (event.type == pg.KEYDOWN and event.key == pg.K_f) or (event.type == pg.MOUSEBUTTONDOWN and event.button == 1):
				weapon_system.start_firing(weapon_system.get_current_weapon())
			
			if (event.type == pg.KEYUP and event.key == pg.K_f) or (event.type == pg.MOUSEBUTTONUP and event.button == 1):
				weapon_system.stop_firing(weapon_system.get_current_weapon())

		dash_system.update(entities, dt)
		input_system.update(player)
		movement_system.update(entities, dt, level_system.level)

		wall_collision_bullets = bullet_collision_system.update(entities, level_system.level)
		entities.difference_update(wall_collision_bullets)
		
		new_deaths = bullet_system.update(entities, level_system.level)
		if player in new_deaths:
			player.get_component(PlayerComponent).is_alive = False
		
		# Remove bullets and dead entities immediately
		entities.difference_update(new_deaths)
		upgrade_system.update(player)
		death_system.deaths.update(new_deaths)
		
		remove = death_system.update()
		entities.difference_update(remove)
		
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
			entities.add(shoot(player_pos, player_rotation, player.id)) # type: ignore

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