import pygame as pg

from game.ecs.components.collider import Collider
from game.ecs.components.speed import Speed
from game.ecs.entity import Entity
from game.ecs.components.physics import Movement, Position, Velocity


class MovementSystem():

    def __init__(self, levelmap: pg.Surface):
        self._collision_mask = pg.mask.from_threshold(levelmap, (0,0,0), (1,1,1))
    
    
    def update(self, entities: set[Entity], dt: float):
        for entity in entities:
            if entity.has_components(Position, Velocity):
                pos: Position = entity.get_component(Position) # type: ignore
                vel: Velocity = entity.get_component(Velocity) # type: ignore
                
                if entity.has_component(Movement):
                    movement: Movement = entity.get_component(Movement) # type: ignore
                    pos.x += round(movement.vx * dt)
                    pos.y += round(movement.vy * dt)
                vel.vx *= 0.95
                vel.vy *= 0.95
                pos.x += round(vel.vx * dt)
                pos.y += round(vel.vy * dt)
                
                # if entity.has_component(Collider):
                #     col: Collider = entity.get_component(Collider) # type: ignore
                #     newx = pos.x + round(vel.vx * dt)
                #     newy = pos.y + round(vel.vy * dt)
                #     if not self._collision_mask.overlap(pg.Mask((col.width, col.height), True), (newx - col.width // 2, newy - col.height // 2)):
                #         pos.x += round(vel.vx * dt)
                #         pos.y += round(vel.vy * dt)
                # else: