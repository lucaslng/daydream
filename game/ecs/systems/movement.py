from game.ecs.System import System
from game.ecs.components.physics import Position, Velocity


class MovementSystem(System):
    def update(self, entities, dt):
        for entity in entities:
            if entity.has_components(Position, Velocity):
                pos = entity.get_component(Position)
                vel = entity.get_component(Velocity)
                pos.x += vel.vx * dt # type: ignore
                pos.y += vel.vy * dt # type: ignore