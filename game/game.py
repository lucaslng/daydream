import pygame as pg

from game.ecs.Entity import Entity
from game.ecs.components.collider import Collider
from game.ecs.components.player import PlayerComponent
from game.ecs.components.person_sprite import PersonSprite
from game.ecs.components.physics import Position, Rotation, Velocity
from game.ecs.components.speed import Speed
from game.ecs.systems.input import InputSystem
from game.ecs.systems.movement import MovementSystem
from game.ecs.systems.render import RenderSystem
from game.sprites.sprite import Sprite
from util.prepare import CLOCK, SURF
from util.screens import Screens
from util.update_screen import update_screen


async def game() -> Screens:
	print("started game!")
	player = Entity()
	player.add_components(Position(100, 100), Velocity(0, 0), Speed(50), PersonSprite(Sprite("player_bodies", "a")), PlayerComponent(), Collider(15, 15), Rotation())
	entities = [player]
	input_system = InputSystem()
	movement_system = MovementSystem()
	render_system = RenderSystem()
	
	while True:
		dt = CLOCK.tick(60) / 1000.0

		for event in pg.event.get():
			if event.type == pg.QUIT:
				raise SystemExit
			if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
				return Screens.MENU
			
		input_system.update(entities, player, dt)
		movement_system.update(entities, player, dt)

		SURF.fill((255, 0, 0))

		render_system.update(entities, player, dt)

		await update_screen()