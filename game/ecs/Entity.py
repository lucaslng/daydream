from game.ecs.Component import Component


class Entity():
	_id_counter = 0

	def __init__(self):
		self.id = Entity._id_counter
		Entity._id_counter += 1
		self.components: dict[type[Component], Component] = {}
	
	def add_component(self, component: Component) -> None:
		self.components[component.__class__] = component

	def add_components(self, *components: Component) -> None:
		for component in components:
			self.add_component(component)
	
	def get_component(self, component_type: type[Component]) -> Component | None:
		return self.components.get(component_type)
	
	def has_component(self, component_type: type[Component]) -> bool:
		return component_type in self.components
	
	def has_components(self, *component_types: type[Component]) -> bool:
		return all([self.has_component(component_type) for component_type in component_types])