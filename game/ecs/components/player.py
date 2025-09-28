from game.ecs.component import Component


class PlayerComponent(Component):
	def __init__(self):
		self.kills = 0
		self.chest = self.legs = self.arms = self.head = False