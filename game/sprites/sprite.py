import pygame as pg

from game.sprites.spritesheet import SpriteSheet


class Sprite():
  SPRITESHEETS: dict[str, SpriteSheet] = {
      "player_bodies": SpriteSheet("spritesheet.png", {"a": (0, 0, 32, 32), "b": (32, 0, 32, 32)}, 4),
      "death_animation": SpriteSheet("death_animation.png", {
          "0": (0, 0, 256, 256),
          "1": (256, 0, 256, 256),
          "2": (512, 0, 256, 256),
          "3": (768, 0, 256, 256),
          "4": (1024, 0, 256, 256),
          "5": (1280, 0, 256, 256),
      })
  }

  def __init__(self, spritesheet: str, sprite_name: str):
    self._spritesheet = spritesheet
    self._sprite_name = sprite_name

  def get(self) -> pg.Surface:
    return Sprite.SPRITESHEETS[self._spritesheet].get(self._sprite_name)
