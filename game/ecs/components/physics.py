from game.ecs.component import Component


class Position(Component):
	def __init__(self, x: int=0, y: int=0):
		self.x = x
		self.y = y

class Velocity(Component):
	def __init__(self, vx: float = 0, vy: float = 0):
		self.vx = vx
		self.vy = vy

class Movement(Component):
	def __init__(self, vx: float = 0, vy: float = 0):
		self.vx = vx
		self.vy = vy
		self.moving = False

class Rotation(Component):
	def __init__(self, angle: float = 0):
		self.angle = angle