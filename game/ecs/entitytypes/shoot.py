from math import cos, radians, sin
from game.ecs.components.bullet import Bullet
from game.ecs.components.collider import Collider
from game.ecs.components.physics import Position, Rotation, Velocity
from game.ecs.components.timer import Timer
from game.ecs.entity import Entity

SPEED = 3267

def shoot(shooter_pos: Position, shooter_rotation: Rotation, shooter_id) -> Entity:
		bullet_dx = SPEED * sin(radians(shooter_rotation.angle))
		bullet_dy = SPEED * -cos(radians(shooter_rotation.angle))
		
		bullet = Entity()
		bullet.add_components(
			Position(shooter_pos.x, shooter_pos.y),
			Velocity(bullet_dx, bullet_dy),
			Collider(12, 12),
			Bullet(shooter_id),
			Rotation(shooter_rotation.angle),
			Timer(.25)
		)
		
		return bullet