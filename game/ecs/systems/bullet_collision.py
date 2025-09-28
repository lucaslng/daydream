import pygame as pg
from game.ecs.components.bullet import Bullet
from game.ecs.components.collider import Collider
from game.ecs.components.physics import Position
from game.ecs.entity import Entity
from game.resources.levels import LEVELS


class BulletCollisionSystem:
	def __init__(self):
		self._collision_masks = [pg.mask.from_surface(pg.transform.scale_by(pg.image.load(
			f"game/resources/collision_masks/collision_mask_{i}.png"), 4)) for i in range(len(LEVELS))]
	
	def update(self, entities: set[Entity], level: int) -> set[Entity]:
		bullets_to_remove: set[Entity] = set()
		
		# Check bullet collision with walls
		for bullet in entities:
			if bullet.has_components(Bullet, Collider, Position):
				bullet_collider: Collider = bullet.get_component(Collider)
				bullet_pos: Position = bullet.get_component(Position)
				
				if self._collision_masks[level].overlap(pg.Mask((bullet_collider.width, bullet_collider.height), True), 
													   (bullet_pos.x - bullet_collider.width//2, bullet_pos.y - bullet_collider.height//2)):
					bullets_to_remove.add(bullet)
		
		return bullets_to_remove
