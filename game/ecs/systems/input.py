import pygame as pg

from game.ecs.System import System
from game.ecs.components.imput import InputComponent
from game.ecs.components.physics import Velocity
from game.ecs.components.speed import Speed

PLAYER_SPEED = 20

class InputSystem(System):
    def update(self, entities, dt):
        keys = pg.key.get_pressed()

        for entity in entities:
            if entity.has_components(InputComponent, Velocity, Speed):
                speed: int = entity.get_component(Speed).speed # type: ignore
                vel: Velocity = entity.get_component(Velocity) # type: ignore

                vel.vx, vel.vy = 0, 0  # reset each frame

                if keys[pg.K_LEFT] or keys[pg.K_a]:
                    vel.vx = -speed
                if keys[pg.K_RIGHT] or keys[pg.K_d]:
                    vel.vx = speed
                if keys[pg.K_UP] or keys[pg.K_w]:
                    vel.vy = -speed
                if keys[pg.K_DOWN] or keys[pg.K_s]:
                    vel.vy = speed