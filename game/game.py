import pygame as pg

from game.ecs.components.bullet import Bullet
from game.ecs.components.circle import Circle
from game.ecs.components.dash import Dash
from game.ecs.components.death import Death
from game.ecs.components.enemy import AStarComponent
from game.ecs.entity import Entity
from game.ecs.components.collider import Collider
from game.ecs.components.player import PlayerComponent
from game.ecs.components.person_sprite import PersonSprite
from game.ecs.components.physics import Movement, Position, Rotation, Velocity
from game.ecs.components.speed import Speed
from game.ecs.entitytypes.enemy import enemy
from game.ecs.entitytypes.shoot import shoot
from game.ecs.systems.astar_system import AStarSystem
from game.ecs.systems.bullets import BulletSystem
from game.ecs.systems.dash import DashSystem
from game.ecs.systems.deaths import DeathSystem
from game.ecs.systems.input import InputSystem
from game.ecs.systems.level_system import LevelSystem
from game.ecs.systems.movement import MovementSystem
from game.ecs.systems.render import RenderSystem
from game.sprites.sprite import Sprite
from game.background import load_game_background, create_game_overlay
from util.prepare import CLOCK, SURF
from util.screens import Screens
from util.update_screen import update_screen


async def game() -> Screens:
	print("started game!")
	player = Entity()
	player.add_components(Position(500, 500), Velocity(0, 0), Speed(500), PersonSprite(Sprite("player_bodies", "a")), PlayerComponent(), Collider(128, 128), Rotation(), Dash(800), Movement())

	# enemy = Entity()
	# enemy.add_components(Death(), Position(500, 400), Velocity(0, 0), Speed(300), PersonSprite(Sprite("player_bodies", "b")), AStarComponent(), Collider(128, 128), Rotation(20), Movement())

	entities = {player}
	level_system = LevelSystem()
	input_system = InputSystem()
	# enemy_ai_system = AStarSystem()
	movement_system = MovementSystem()
	dash_system = DashSystem()
	bullet_system = BulletSystem()
	death_system = DeathSystem()
	render_system = RenderSystem()
	
	background = load_game_background()
	overlay = create_game_overlay()

	entities.update(level_system.get_enemies())
	
	while True:
		dt = CLOCK.tick(60) / 1000.0

		for event in pg.event.get():
			if event.type == pg.QUIT:
				raise SystemExit
			if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
				return Screens.MENU
			# if event.type == pg.KEYDOWN and event.key == pg.K_i:
			# 	return Screens.GAMEOVER
			# if event.type == pg.KEYDOWN and event.key == pg.K_o:
			# 	return Screens.LEVELCLEAR
			if (event.type == pg.KEYDOWN and event.key == pg.K_f) or (event.type == pg.MOUSEBUTTONDOWN and event.button == 1):
				print("hi")
				player_pos = player.get_component(Position)
				player_rotation = player.get_component(Rotation)
				entities.add(shoot(player_pos, player_rotation, player.id)) # type: ignore
			# return Screens.INGAMEMENU

		dash_system.update(entities, dt)
		input_system.update(player)
		# enemy_ai_system.update(entities, player, [[True for _ in range(1000)] for __ in range(1000)], dt)
		movement_system.update(entities, dt, level_system.level)

		new_deaths = bullet_system.update(entities)
		if player in new_deaths:
			return Screens.GAMEOVER
		
		death_system.deaths.update(new_deaths)
		
		remove = death_system.update()
		entities.difference_update(remove)

		SURF.blit(background, (0, 0))
		SURF.blit(overlay, (0, 0))

		render_system.update(entities, player, level_system.level)

		await update_screen()