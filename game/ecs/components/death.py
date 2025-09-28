from game.ecs.component import Component


class Death(Component):
	def __init__(self):
		self.death = False
		self.frame = 0