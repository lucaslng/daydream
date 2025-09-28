from game.ecs.component import Component


class Timer(Component):
	def __init__(self, duration: float):
		self.duration = duration
		self.time_left = duration
	
	def is_expired(self) -> bool:
		return self.time_left <= 0
	
	def update(self, dt: float):
		self.time_left -= dt
