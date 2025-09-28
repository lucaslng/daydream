from math import degrees, atan2, cos, sin, radians
import pygame as pg

from game.ecs.components.dash import Dash
from game.ecs.entity import Entity
from game.ecs.components.physics import Movement, Rotation, Velocity
from game.ecs.components.speed import Speed
from util.prepare import WINDOW

PLAYER_SPEED = 20


class InputSystem():
  def update(self, player: Entity):
    movement: Movement = player.get_component(Movement) # type: ignore
    movement.moving = False
    keys = pg.key.get_pressed()
    speed: int = player.get_component(Speed).speed  # type: ignore
    vel: Velocity = player.get_component(Velocity)  # type: ignore
    rotation: Rotation = player.get_component(Rotation) #type: ignore

    mouse_pos = pg.mouse.get_pos()
    rotation.angle = degrees(atan2(mouse_pos[1] - WINDOW[1] / 2, mouse_pos[0] - WINDOW[0] / 2)) + 90

    movement.vx, movement.vy = 0, 0  # reset each frame

    if keys[pg.K_LEFT] or keys[pg.K_a]:
      movement.vx = -speed
      movement.moving = True
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
      movement.vx = speed
      movement.moving = True
    if keys[pg.K_UP] or keys[pg.K_w]:
      movement.vy = -speed
      movement.moving = True
    if keys[pg.K_DOWN] or keys[pg.K_s]:
      movement.vy = speed
      movement.moving = True
    if keys[pg.K_SPACE]:
      dash: Dash = player.get_component(Dash) # type: ignore
      if dash.dash_timer <= 0.0:
        dash.dash_timer = dash.dash_cooldown
        vel.vx += dash.dash_speed * sin(radians(rotation.angle))
        vel.vy += dash.dash_speed * -cos(radians(rotation.angle))
