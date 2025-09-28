import pygame as pg
from math import cos, sin, radians

from game.ecs.components.bullet import Bullet
from game.ecs.components.physics import Position, Velocity, Rotation
from game.ecs.components.collider import Collider
from game.ecs.components.person_sprite import PersonSprite
from game.sprites.sprite import Sprite
from game.ecs.entity import Entity


class ShootingSystem:
	def __init__(self):
		self.bullet_speed = 3000
		self.bullet_scale = 0.75  #scaled down might change later
	
	def create_bullet(self, shooter_pos: Position, shooter_rotation: Rotation, shooter_id) -> Entity:
		"""Create a bullet that shoots forward from the player's position"""
		bullet_dx = self.bullet_speed * sin(radians(shooter_rotation.angle))
		bullet_dy = self.bullet_speed * -cos(radians(shooter_rotation.angle))
		
		bullet = Entity()
		bullet.add_components(
			Position(shooter_pos.x, shooter_pos.y),
			Velocity(bullet_dx, bullet_dy),
			Collider(12, 12),  #scaled collision box !!!!!!!!!!! sync with self.bullet_scale please
			Bullet(shooter_id),
			Rotation(shooter_rotation.angle)
		)
		
		return bullet
