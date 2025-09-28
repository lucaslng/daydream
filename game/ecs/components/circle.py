from game.ecs.component import Component


class Circle(Component):
	def __init__(self, size: int, color: tuple):
		self.size = size
		self.color = color