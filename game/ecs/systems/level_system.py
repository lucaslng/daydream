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
		self.level_times = [0.0, 0.0, 0.0]
		self.is_level_complete = False
	
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
	
	def check_level_complete(self) -> bool:
		return self.enemies_remaining <= 0
	
	def get_level_time(self) -> float:
		return time.time() - self.level_start_time
	
	def get_total_time(self) -> float:
		return time.time() - self.start_time
		
	def get_enemies(self) -> list[Entity]:
		if self.level < len(LEVELS):
			return [enemy(Position(*p.pos)) for p in LEVELS[self.level].enemies]
		else:
			return []
	
	def update(self, entities: set[Entity]):
		self.enemies_remaining = 0
		for entity in entities:
			if entity.has_component(Enemy):
				self.enemies_remaining += 1
	
	def complete_level(self):
		self.level_times[self.level] = self.get_level_time()
		self.is_level_complete = True
	
	def next_level(self):
		self.level += 1
		if self.level < len(LEVELS):
			self.enemies_remaining = len(LEVELS[self.level].enemies)
			self.level_start_time = time.time()
			self.is_level_complete = False
		else:
			self.is_level_complete = True
	
	def is_game_complete(self) -> bool:
		return self.level >= len(LEVELS)
	
	def get_total_time(self) -> float:
		return sum(self.level_times)
	
	def get_level_spawn(self):
		if self.level < len(LEVELS):
			return Position(*LEVELS[self.level].spawn_pos)
		else:
			return Position(500, 500)