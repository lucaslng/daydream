import time
import math
import pygame as pg
from game.ecs.components.enemy import Enemy
from game.ecs.components.physics import Position, Rotation
from game.ecs.components.weapon import Weapon
from game.ecs.entity import Entity
from game.ecs.entitytypes.shoot import shoot
from game.resources.levels import LEVELS


class EnemyAISystem:
	def __init__(self):
		self.last_shot_times = {}
		self.shoot_cooldown = 3.0
		self.shoot_range = 400
		self._collision_masks = [pg.mask.from_surface(pg.transform.scale_by(pg.image.load(
			f"game/resources/collision_masks/collision_mask_{i}.png"), 4)) for i in range(len(LEVELS))]
	
	def configure(self, cooldown: float = None, range: float = None):
		if cooldown is not None:
			self.shoot_cooldown = cooldown
		if range is not None:
			self.shoot_range = range
	
	def update(self, entities: set[Entity], player: Entity, level: int = 0):
		player_pos = player.get_component(Position)
		player_rotation = player.get_component(Rotation)
		
		entities_copy = list(entities)
		for entity in entities_copy:
			if entity.has_components(Enemy, Position, Rotation, Weapon):
				enemy_pos = entity.get_component(Position)
				enemy_rotation = entity.get_component(Rotation)
				enemy_weapon = entity.get_component(Weapon)
				
				dx = player_pos.x - enemy_pos.x
				dy = player_pos.y - enemy_pos.y
				distance = math.sqrt(dx*dx + dy*dy)
				
				angle_to_player = math.degrees(math.atan2(dy, dx)) + 90
				
				enemy_rotation.angle = angle_to_player
				
				if distance < self.shoot_range and self._has_line_of_sight(enemy_pos, player_pos, level):
					if self._can_shoot(enemy_weapon):
						self._shoot_weapon(enemy_weapon)
						bullet = shoot(enemy_pos, enemy_rotation, entity.id)
						entities.add(bullet)
	
	def _can_shoot(self, weapon: Weapon) -> bool:
		current_time = time.time()
		return current_time - weapon.last_shot_time >= weapon.fire_rate
	
	def _shoot_weapon(self, weapon: Weapon):
		weapon.last_shot_time = time.time()
	
	def _has_line_of_sight(self, start_pos: Position, end_pos: Position, level: int) -> bool:
		if level >= len(self._collision_masks):
			return True
		
		steps = 20
		dx = (end_pos.x - start_pos.x) / steps
		dy = (end_pos.y - start_pos.y) / steps
		
		for i in range(steps + 1):
			check_x = start_pos.x + dx * i
			check_y = start_pos.y + dy * i
			
			if self._collision_masks[level].overlap(pg.Mask((8, 8), True), 
												   (check_x - 4, check_y - 4)):
				return False
		
		return True
