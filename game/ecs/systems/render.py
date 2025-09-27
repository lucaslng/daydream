from game.ecs.System import System
import pygame as pg

from game.ecs.components.physics import Position, Rotation
from game.ecs.components.person_sprite import PersonSprite
from util.prepare import SURF


class RenderSystem(System):

	def update(self, entities, player, dt):
		for entity in entities:
			if entity.has_component(Position) and entity.has_component(PersonSprite):
				pos: Position = entity.get_component(Position) # type: ignore
				angle: float = entity.get_component(Rotation).angle # type: ignore
				person_sprite: PersonSprite = entity.get_component(PersonSprite) # type: ignore
				rotated = pg.transform.rotate(person_sprite.body_sprite.get(), -angle) # type: ignore
				SURF.blit(rotated, rotated.get_rect(center=SURF.get_rect().center))