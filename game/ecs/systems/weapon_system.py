import time
from game.ecs.components.weapon import Weapon
from game.ecs.entity import Entity


class WeaponSystem:
	def __init__(self):
		self.current_weapon_index = 0
		self.weapons = [
			Weapon("ar", 0.15, 4, 1.0),
			Weapon("lmg", 0.05, 1, 0.0),
			Weapon("revolver", 0.8, 1, 0.0)
		]
		self.weapon_names = ["ar", "lmg", "revolver"]
	
	def switch_weapon(self, direction: int = 1):
		self.current_weapon_index = (self.current_weapon_index + direction) % len(self.weapons)
		return self.weapons[self.current_weapon_index]
	
	def get_current_weapon(self):
		return self.weapons[self.current_weapon_index]
	
	def start_firing(self, weapon: Weapon):
		weapon.is_firing = True
		weapon.shots_in_burst = 0
	
	def stop_firing(self, weapon: Weapon):
		weapon.is_firing = False
	
	def can_shoot(self, weapon: Weapon) -> bool:
		current_time = time.time()
		
		if weapon.weapon_type == "lmg":
			# LMG: Full auto
			return weapon.is_firing and (current_time - weapon.last_shot_time >= weapon.fire_rate)
		elif weapon.weapon_type == "ar":
			# AR: Burst fire
			if weapon.shots_in_burst >= weapon.burst_count:
				if current_time - weapon.last_burst_time >= weapon.burst_delay:
					weapon.shots_in_burst = 0
					weapon.last_burst_time = current_time
					return True
				return False
			else:
				return weapon.is_firing and (current_time - weapon.last_shot_time >= weapon.fire_rate)
		elif weapon.weapon_type == "revolver":
			# Revolver: Single shot
			return weapon.is_firing and (current_time - weapon.last_shot_time >= weapon.fire_rate)
		
		return False
	
	def shoot(self, weapon: Weapon) -> bool:
		if not self.can_shoot(weapon):
			return False
		
		current_time = time.time()
		weapon.last_shot_time = current_time
		weapon.shots_in_burst += 1
		
		return True
