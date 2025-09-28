from game.ecs.components.physics import Position
from game.ecs.entity import Entity
from game.ecs.entitytypes.enemy import enemy
from game.resources.levels import LEVELS

class LevelSystem():

	def __init__(self):
		self.level = 0
	
	def get_enemies(self):
		enemies: set[Entity] = set()
		for enemy_info in LEVELS[self.level].enemies:
			enemies.add(enemy(Position(*enemy_info.pos)))
		return enemies