from game.ecs.components.enemy import Enemy
from game.ecs.components.physics import Position
from game.ecs.entity import Entity
from game.ecs.entitytypes.enemy import enemy
from game.resources.levels import LEVELS

class LevelSystem():

	def __init__(self):
		self.level = 0
		self.enemies_remaining = len(LEVELS[self.level].enemies)
	
	def get_enemies(self):
		enemies: set[Entity] = set()
		for enemy_info in LEVELS[self.level].enemies:
			enemies.add(enemy(Position(*enemy_info.pos)))
		return enemies
	
	def update(self, entities: set[Entity]):
		self.enemies_remaining = 0
		for entity in entities:
			if entity.has_component(Enemy):
				self.enemies_remaining += 1
	
	def next_level(self):
		self.level += 1
		self.enemies_remaining = len(LEVELS[self.level].enemies)
	
	def get_level_spawn(self):
		return Position(*LEVELS[self.level].spawn_pos)