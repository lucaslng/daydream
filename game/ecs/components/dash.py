from game.ecs.component import Component


class Dash(Component):
	def __init__(self, dash_speed: int) -> None:
		self.dash_speed = dash_speed
		self.dash_timer = 0.0
		self.dash_cooldown = 2.0