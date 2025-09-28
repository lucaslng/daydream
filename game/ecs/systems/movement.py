import pygame as pg

from game.ecs.components.collider import Collider
from game.ecs.components.speed import Speed
from game.ecs.entity import Entity
from game.ecs.components.physics import Movement, Position, Velocity
from game.resources.levels import LEVELS
from util.prepare import SURF


class MovementSystem():

  def __init__(self):
    self._collision_masks = [pg.mask.from_surface(pg.transform.scale_by(pg.image.load(
      f"game/resources/collision_masks/collision_mask_{i}.png"), 4)) for i in range(len(LEVELS))]

  def update(self, entities: set[Entity], dt: float, level: int):
    
    for entity in entities:
      if entity.has_components(Position, Velocity):
        pos: Position = entity.get_component(Position)  # type: ignore
        vel: Velocity = entity.get_component(Velocity)  # type: ignore

        if entity.has_component(Collider):
          col: Collider = entity.get_component(Collider)  # type: ignore
          newx = pos.x
          newy = pos.y
          if entity.has_component(Movement):
            movement: Movement = entity.get_component(Movement)  # type: ignore
            newx += round(movement.vx * dt)
            newy += round(movement.vy * dt)
          newx += round(vel.vx * dt * 0.95)
          newy += round(vel.vy * dt * 0.95)
          if self._collision_masks[level].overlap(pg.Mask((col.width, col.height), True), (newx - col.width//2, newy - col.height//2)):
            continue

        if entity.has_component(Movement):
          movement: Movement = entity.get_component(Movement)  # type: ignore
          pos.x += round(movement.vx * dt)
          pos.y += round(movement.vy * dt)
        vel.vx *= 0.95
        vel.vy *= 0.95
        pos.x += round(vel.vx * dt)
        pos.y += round(vel.vy * dt)
