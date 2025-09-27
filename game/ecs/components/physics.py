from game.ecs.Component import Component


class Position(Component):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

class Velocity(Component):
	def __init__(self, vx=0, vy=0):
		self.vx = vx
		self.vy = vy

class Rotation(Component):
	def __init__(self, angle: float = 0):
		self.angle = angle