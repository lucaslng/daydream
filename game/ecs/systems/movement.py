import pygame as pg

from game.ecs.components.bullet import Bullet
from game.ecs.components.collider import Collider
from game.ecs.entity import Entity
from game.ecs.components.physics import Movement, Position, Velocity
from game.resources.levels import LEVELS


class MovementSystem():

  def __init__(self):
    self._collision_masks = [pg.mask.from_surface(pg.transform.scale_by(pg.image.load(
      f"game/resources/collision_masks/collision_mask_{i}.png"), 4)) for i in range(len(LEVELS))]

  def update(self, entities: set[Entity], dt: float, level: int):
    
    for entity in entities:
      if entity.has_components(Position, Velocity):
        pos: Position = entity.get_component(Position)
        vel: Velocity = entity.get_component(Velocity)

        if entity.has_component(Collider):
          col: Collider = entity.get_component(Collider)
          total_vx = 0
          total_vy = 0
          
          if entity.has_component(Movement):
            movement: Movement = entity.get_component(Movement)
            total_vx += round(movement.vx * dt)
            total_vy += round(movement.vy * dt)
          
          total_vx += round(vel.vx * dt * 0.95)
          total_vy += round(vel.vy * dt * 0.95)
          
          if entity.has_component(Bullet):
            newx = pos.x + total_vx
            newy = pos.y + total_vy
            if level < len(self._collision_masks) and self._collision_masks[level].overlap(pg.Mask((col.width, col.height), True), 
                                                   (newx - col.width//2, newy - col.height//2)):
              total_vx = 0
              total_vy = 0
            pos.x += total_vx
            pos.y += total_vy
          else:
            newx = pos.x + total_vx
            if level < len(self._collision_masks) and self._collision_masks[level].overlap(pg.Mask((col.width, col.height), True), 
                                                   (newx - col.width//2, pos.y - col.height//2)):
              total_vx = 0
            
            newy = pos.y + total_vy
            if level < len(self._collision_masks) and self._collision_masks[level].overlap(pg.Mask((col.width, col.height), True), 
                                                   (pos.x - col.width//2, newy - col.height//2)):
              total_vy = 0
            
            pos.x += total_vx
            pos.y += total_vy
          
        else:
          if entity.has_component(Movement):
            movement: Movement = entity.get_component(Movement)
            pos.x += round(movement.vx * dt)
            pos.y += round(movement.vy * dt)
          pos.x += round(vel.vx * dt * 0.95)
          pos.y += round(vel.vy * dt * 0.95)
        
        vel.vx *= 0.95
        vel.vy *= 0.95