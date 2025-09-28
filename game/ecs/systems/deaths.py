from game.ecs.components.death import Death
from game.ecs.entity import Entity


class DeathSystem():
	def __init__(self):
		self.deaths: set[Entity] = set()
	
	def reset_entity_death(self, entity: Entity):
		if entity.has_component(Death):
			death = entity.get_component(Death)
			death.death = False
			death.frame = 0
		self.deaths.discard(entity)
	
	def update(self) -> set[Entity]:
		remove: set[Entity] = set()
		for entity in self.deaths:
			if entity.has_component(Death):
				death: Death = entity.get_component(Death)
				if death.death:
					death.frame += 1
					if death.frame >= 11:
						remove.add(entity)
				else:
					death.death = True
			else:
				remove.add(entity)
		
		self.deaths.difference_update(remove)
		return remove