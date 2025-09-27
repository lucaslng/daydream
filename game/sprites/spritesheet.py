import pygame as pg

class SpriteSheet:
    """sprite sheet class"""

    def __init__(self, filename: str, sprites: dict[str, tuple[int, int, int, int]]) -> None:
        self.sheet = pg.image.load(f"game/resources/spritesheets/{filename}").convert_alpha()
        self._sprites = sprites

    def _get(self, x: int, y: int, width: int, height: int) -> pg.Surface:
        image = pg.Surface((width, height), pg.SRCALPHA)
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        return image
    
    def get(self, sprite: str) -> pg.Surface:
        return self._get(*self._sprites[sprite])