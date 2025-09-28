import pygame as pg

from game.sprites.spritesheet import SpriteSheet


class Sprite():
  SPRITESHEETS: dict[str, SpriteSheet] = {
      "player_bodies": SpriteSheet("spritesheet.png", {
          "a": (128, 0, 32, 32),
          "b": (160, 0, 32, 32)
        }, 4),
      "weapons": SpriteSheet("spritesheet.png", {
          "assault_rifle": (0, 0, 32, 32),
          "bullet": (32, 0, 32, 32),
          "lmg": (64, 0, 32, 32),
          "revolver": (96, 0, 32, 32)
        }, 4),
      "death_animation": SpriteSheet("death_animation.png", {
          "0": (0, 0, 256, 256),
          "1": (256, 0, 256, 256),
          "2": (512, 0, 256, 256),
          "3": (768, 0, 256, 256),
          "4": (1024, 0, 256, 256),
          "5": (1280, 0, 256, 256),
      }),
      "body": SpriteSheet("body.png", {
          "base_head": (0, 0, 128, 190),
          "base_chest": (128, 0, 128, 190),
          "base_arms": (256, 0, 128, 190),
          "base_legs": (384, 0, 128, 190),
          "upgraded_head": (512, 0, 128, 190),
          "upgraded_chest": (640, 0, 128, 190),
          "upgraded_arms_top": (768, 0, 128, 190),
          "upgraded_arms_bottom": (896, 0, 128, 190),
          "upgraded_legs_top": (1024, 0, 128, 190),
          "upgraded_legs_bottom": (1152, 0, 128, 190),
      }, 1.4)
  }

  def __init__(self, spritesheet: str, sprite_name: str):
    self._spritesheet = spritesheet
    self._sprite_name = sprite_name

  def get(self) -> pg.Surface:
    return Sprite.SPRITESHEETS[self._spritesheet].get(self._sprite_name)
