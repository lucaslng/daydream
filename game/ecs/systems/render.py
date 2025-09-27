from game.ecs.System import System
import pygame as pg

from game.ecs.components.physics import Position
from game.ecs.components.person_sprite import PersonSprite
from util.prepare import SURF


class RenderSystem(System):
	def __init__(self, surf: pg.Surface):
		self.surf = surf

	def update(self, entities, dt):
		for entity in entities:
			if entity.has_component(Position) and entity.has_component(PersonSprite):
				pos: Position = entity.get_component(Position) # type: ignore
				person_sprite: PersonSprite = entity.get_component(PersonSprite) # type: ignore
				SURF.blit(person_sprite.body_sprite.get(), (pos.x, pos.y))