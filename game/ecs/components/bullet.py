from game.ecs.component import Component


class Bullet(Component):
	def __init__(self, shooter_id: int):
		self.shooter_id = shooter_id