from game.ecs.components.collider import Collider
from game.ecs.components.death import Death
from game.ecs.components.astar import AStarComponent
from game.ecs.components.enemy import Enemy
from game.ecs.components.person_sprite import PersonSprite
from game.ecs.components.physics import Movement, Position, Rotation, Velocity
from game.ecs.components.speed import Speed
from game.ecs.entity import Entity
from game.sprites.sprite import Sprite


def enemy(position: Position):
	enemy = Entity()
	enemy.add_components(Death(), position, Enemy(), Velocity(0, 0), Speed(300), PersonSprite(Sprite("player_bodies", "b")), AStarComponent(), Collider(128, 128), Rotation(20), Movement())
	return enemy