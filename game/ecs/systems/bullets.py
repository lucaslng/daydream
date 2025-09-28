import pygame as pg
from pygame import Rect

from game.ecs.components.bullet import Bullet
from game.ecs.components.collider import Collider
from game.ecs.components.death import Death
from game.ecs.components.person_sprite import PersonSprite
from game.ecs.components.physics import Position
from game.ecs.components.player import PlayerComponent
from game.ecs.entity import Entity
from game.resources.levels import LEVELS
from game.resources.sfx.sfx import boom_sound


class BulletSystem():
	def __init__(self):
		self._collision_masks = [pg.mask.from_surface(pg.transform.scale_by(pg.image.load(
			f"game/resources/collision_masks/collision_mask_{i}.png"), 4)) for i in range(len(LEVELS))]
	
	def update(self, entities: set[Entity], level: int) -> set[Entity]:
		deaths: set[Entity] = set()
		bullets_to_remove: set[Entity] = set()
		
		for bullet in entities:
			if bullet.has_components(Bullet, Collider, Position):
				bullet_collider: Collider = bullet.get_component(Collider)
				bullet_pos: Position = bullet.get_component(Position)
				
				if self._collision_masks[level].overlap(pg.Mask((bullet_collider.width, bullet_collider.height), True), 
													   (bullet_pos.x - bullet_collider.width//2, bullet_pos.y - bullet_collider.height//2)):
					bullets_to_remove.add(bullet)
		
		for entity in entities:
			if entity.has_components(PersonSprite, Collider, Position):
				if entity.has_component(Death) and entity.get_component(Death).death:
					continue
				for bullet in entities:
					if bullet.has_components(Bullet, Collider, Position) and bullet.get_component(Bullet).shooter_id != entity.id:
						entity_collider: Collider = entity.get_component(Collider)
						entity_pos: Position = entity.get_component(Position)
						bullet_collider: Collider = bullet.get_component(Collider)
						bullet_pos: Position = bullet.get_component(Position)
						entity_rect = Rect()
						entity_rect.center = entity_pos.x, entity_pos.y
						entity_rect.size = entity_collider.width, entity_collider.height
						bullet_rect = Rect()
						bullet_rect.center = bullet_pos.x, bullet_pos.y
						bullet_rect.size = bullet_collider.width, bullet_collider.height
						if entity_rect.colliderect(bullet_rect):
							boom_sound.play()
							if entity.has_component(PlayerComponent):
								deaths.add(entity)
							else:
								if entity.has_component(Death):
									entity.get_component(Death).death = True
								else:
									entity.add_component(Death())
								deaths.add(entity)
							bullets_to_remove.add(bullet)
							
							shooter_id = bullet.get_component(Bullet).shooter_id
							for potential_shooter in entities:
								if potential_shooter.id == shooter_id and potential_shooter.has_component(PlayerComponent):
									player_comp = potential_shooter.get_component(PlayerComponent)
									player_comp.kills += 1
		
		deaths.update(bullets_to_remove)
		return deaths
						