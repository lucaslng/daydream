from game.ecs.component import Component


class Speed(Component):
	def __init__(self, speed: int) -> None:
		self.speed = speed