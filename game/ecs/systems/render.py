from game.ecs.System import System
import pygame as pg

from game.ecs.components.circle import Circle
from game.ecs.components.physics import Position


class RenderSystem(System):
	def __init__(self, screen):
		self.screen = screen

	def update(self, entities, dt):
		for entity in entities:
			if entity.has_component(Position) and entity.has_component(Circle):
				pos = entity.get_component(Position)
				circle = entity.get_component(Circle)
				pg.draw.circle(self.screen, circle.color, (int(pos.x), int(pos.y)), circle.size) # type: ignore