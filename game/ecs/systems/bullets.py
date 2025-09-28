from pygame import Rect

from game.ecs.components.bullet import Bullet
from game.ecs.components.collider import Collider
from game.ecs.components.death import Death
from game.ecs.components.person_sprite import PersonSprite
from game.ecs.components.physics import Position
from game.ecs.entity import Entity


class BulletSystem():
	def update(self, entities: set[Entity]) -> set[Entity]:
		deaths: set[Entity] = set()
		for entity in entities:
			if entity.has_components(PersonSprite, Collider, Position) and (not entity.has_component(Death) or (entity.has_component(Death) and not entity.get_component(Death).death)):
				for bullet in entities:
					if bullet.has_components(Bullet, Collider, Position):
						entity_collider: Collider = entity.get_component(Collider) # type: ignore
						entity_pos: Position = entity.get_component(Position) # type: ignore
						bullet_collider: Collider = bullet.get_component(Collider) # type: ignore
						bullet_pos: Position = bullet.get_component(Position) # type: ignore
						entity_rect = Rect()
						entity_rect.center = entity_pos.x, entity_pos.y
						entity_rect.size = entity_collider.width, entity_collider.height
						bullet_rect = Rect()
						bullet_rect.center = bullet_pos.x, bullet_pos.y
						bullet_rect.size = bullet_collider.width, bullet_collider.height
						if entity_rect.colliderect(bullet_rect):
							deaths.add(entity)
		return deaths
						