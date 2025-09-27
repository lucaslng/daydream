import pygame as pg

from game.sprites.spritesheet import SpriteSheet

class Sprite():
	SPRITESHEETS: dict[str, SpriteSheet] = {
	"player_bodies": SpriteSheet("spritesheet.png", {"a": (0, 0, 32, 32), "b": (32, 0, 32, 32)}, 4)
}
	
	def __init__(self, spritesheet: str, sprite_name: str):
		self._spritesheet = spritesheet
		self._sprite_name = sprite_name

	def get(self) -> pg.Surface:
		return self.SPRITESHEETS[self._spritesheet].get(self._sprite_name)