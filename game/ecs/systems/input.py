from math import degrees, atan2
import pygame as pg

from game.ecs.System import System
from game.ecs.components.physics import Position, Rotation, Velocity
from game.ecs.components.speed import Speed
from util.prepare import SURF, WINDOW

PLAYER_SPEED = 20


class InputSystem(System):
  def update(self, entities, player, dt):
    keys = pg.key.get_pressed()
    speed: int = player.get_component(Speed).speed  # type: ignore
    vel: Velocity = player.get_component(Velocity)  # type: ignore
    rotation: Rotation = player.get_component(Rotation) #type: ignore

    mouse_pos = pg.mouse.get_pos()
    rotation.angle = degrees(atan2(mouse_pos[1] - WINDOW[1] / 2, mouse_pos[0] - WINDOW[0] / 2)) + 90

    vel.vx, vel.vy = 0, 0  # reset each frame

    if keys[pg.K_LEFT] or keys[pg.K_a]:
      vel.vx = -speed
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
      vel.vx = speed
    if keys[pg.K_UP] or keys[pg.K_w]:
      vel.vy = -speed
    if keys[pg.K_DOWN] or keys[pg.K_s]:
      vel.vy = speed
