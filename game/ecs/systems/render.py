import pygame as pg

from game.ecs.components.circle import Circle
from game.ecs.entity import Entity
from game.ecs.components.physics import Position, Rotation
from game.ecs.components.person_sprite import PersonSprite
from util.prepare import SURF


class RenderSystem():

	def update(self, entities: list[Entity], player: Entity, map: pg.Surface):
		# draw player 

		player_pos: Position = player.get_component(Position) # type: ignore
		offset_x = SURF.get_rect().centerx - player_pos.x
		offset_y = SURF.get_rect().centery - player_pos.y

		for entity in entities:
			if entity.has_component(Position):
				entity_pos: Position = entity.get_component(Position) # type: ignore
				new_pos = (entity_pos.x + offset_x, entity_pos.y + offset_y)
				if entity.has_components(PersonSprite, Rotation):
					angle: float = entity.get_component(Rotation).angle # type: ignore
					person_sprite: PersonSprite = entity.get_component(PersonSprite) # type: ignore
					rotated = pg.transform.rotate(person_sprite.body_sprite.get(), -angle) # type: ignore
					
					SURF.blit(rotated, rotated.get_rect(center=new_pos))
				if entity.has_component(Circle):
					circle: Circle = entity.get_component(Circle) # type: ignore
					pg.draw.circle(SURF, circle.color, new_pos, circle.size)
				