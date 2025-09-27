from game.ecs.Component import Component


class Sprite(Component):
	def __init__(self, sprite):
		self.sprite = sprite