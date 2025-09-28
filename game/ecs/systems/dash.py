from game.ecs.components.dash import Dash
from game.ecs.entity import Entity


class DashSystem():
	def update(self, entities: set[Entity], dt: float):
		for entity in entities:
			if entity.has_component(Dash):
				dash: Dash = entity.get_component(Dash) # type: ignore
				dash.dash_timer -= dt