from pygame import Color
import pygame as pg
from game.ecs.Entity import Entity
from game.ecs.components.circle import Circle
from game.ecs.components.imput import InputComponent
from game.ecs.components.physics import Position, Velocity
from game.ecs.components.speed import Speed
from game.ecs.systems.input import InputSystem
from game.ecs.systems.movement import MovementSystem
from game.ecs.systems.render import RenderSystem
from util.prepare import CLOCK, SURF
from util.screens import Screens
from util.update_screen import update_screen


async def game() -> Screens:
	print("started game!")
	player = Entity()
	player.add_component(Position(100, 100))
	player.add_component(Velocity(0, 0))
	player.add_component(Speed(50))
	player.add_component(Circle(15, (0, 255, 0)))
	player.add_component(InputComponent())
	entities = [player]
	input_system = InputSystem()
	movement_system = MovementSystem()
	render_system = RenderSystem(SURF)
	while True:
		dt = CLOCK.tick(60) / 1000.0

		for event in pg.event.get():
			if event.type == pg.QUIT:
				raise SystemExit
			if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
				return Screens.MENU
			
		input_system.update(entities, dt)
		movement_system.update(entities, dt)

		SURF.fill((255, 0, 0))

		render_system.update(entities, dt)

		await update_screen()