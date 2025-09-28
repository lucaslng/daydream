from game.ecs.component import Component


class Weapon(Component):
	def __init__(self, weapon_type: str, fire_rate: float, burst_count: int = 1, burst_delay: float = 0.0):
		self.weapon_type = weapon_type  # "ar", "lmg", "revolver"
		self.fire_rate = fire_rate  # Time between shots
		self.burst_count = burst_count  # Shots per burst (1 for full auto)
		self.burst_delay = burst_delay  # Delay between bursts
		self.last_shot_time = 0.0
		self.shots_in_burst = 0
		self.last_burst_time = 0.0
		self.is_firing = False
