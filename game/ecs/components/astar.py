from game.ecs.component import Component


class AStarComponent(Component):
	def __init__(self):
		self.path: list[tuple[int, int]] = []
		self.target_index = 0