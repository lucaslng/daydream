import pygame as pg

class SpriteSheet:
    """sprite sheet class"""

    def __init__(self, filename: str, sprites: dict[str, tuple[int, int, int, int]], scale_by: int | None = None) -> None:
        self.sheet = pg.image.load(f"game/resources/spritesheets/{filename}").convert_alpha()
        if scale_by:
            assert scale_by > 1
            self.sheet = pg.transform.scale_by(self.sheet, scale_by)
        self._scale_by = scale_by
        self._sprites = sprites

    def _get(self, x: int, y: int, width: int, height: int) -> pg.Surface:
        if self._scale_by:
            x *= self._scale_by
            y *= self._scale_by
            width *= self._scale_by
            height *= self._scale_by
        image = pg.Surface((width, height), pg.SRCALPHA)
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        return image
    
    def get(self, sprite: str) -> pg.Surface:
        return self._get(*self._sprites[sprite])