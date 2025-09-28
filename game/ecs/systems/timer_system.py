from game.ecs.components.timer import Timer
from game.ecs.entity import Entity


class TimerSystem:
	def update(self, entities: set[Entity], dt: float) -> set[Entity]:
		entities_to_remove = set()
		
		for entity in entities:
			if entity.has_component(Timer):
				timer = entity.get_component(Timer)
				timer.update(dt)
				
				if timer.is_expired():
					entities_to_remove.add(entity)
		
		return entities_to_remove
