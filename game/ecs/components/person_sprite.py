from game.ecs.component import Component
from game.sprites.sprite import Sprite


class PersonSprite(Component):
	def __init__(self, body_sprite: Sprite):
		self.body_sprite = body_sprite