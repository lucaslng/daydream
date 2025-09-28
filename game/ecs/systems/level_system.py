import time
from game.ecs.components.player import PlayerComponent
from game.ecs.components.enemy import Enemy
from game.ecs.components.physics import Position
from game.ecs.entity import Entity
from game.ecs.entitytypes.enemy import enemy
from game.resources.levels import LEVELS


class LevelSystem:
	def __init__(self):
		self.level = 2
		self.enemies_remaining = len(LEVELS[self.level].enemies)
		self.start_time = time.time()
		self.level_start_time = time.time()
		self.total_players = 0
		self.alive_players = 0
	
	def start_level(self, entities: set[Entity]):
		self.level_start_time = time.time()
		self.total_players = 0
		self.alive_players = 0
		
		for entity in entities:
			if entity.has_component(PlayerComponent):
				self.total_players += 1
				if entity.get_component(PlayerComponent).is_alive:
					self.alive_players += 1
	
	def update_player_count(self, entities: set[Entity]):
		self.alive_players = 0
		for entity in entities:
			if entity.has_component(PlayerComponent):
				if entity.get_component(PlayerComponent).is_alive:
					self.alive_players += 1
	
	def is_level_complete(self) -> bool:
		return self.alive_players <= 0
	
	def get_level_time(self) -> float:
		return time.time() - self.level_start_time
	
	def get_total_time(self) -> float:
		return time.time() - self.start_time
		
	def get_enemies(self) -> list[Entity]:
		return [enemy(Position(*p.pos)) for p in LEVELS[self.level].enemies]
	
	def update(self, entities: set[Entity]):
		self.enemies_remaining = 0
		for entity in entities:
			if entity.has_component(Enemy):
				self.enemies_remaining += 1
	
	def next_level(self):
		self.level += 1
		self.enemies_remaining = len(LEVELS[self.level].enemies)
		self.level_start_time = time.time()
	
	def get_level_spawn(self):
		return Position(*LEVELS[self.level].spawn_pos)