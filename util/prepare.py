import pygame as pg


FPS = 60
WINDOW = (1200, 720)
CLOCK = pg.time.Clock()
SURF = pg.display.set_mode(WINDOW)

pg.init()
pg.event.set_allowed([pg.QUIT, pg.KEYDOWN, pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP])
pg.font.init()
pg.mixer.init()
pg.mixer.set_reserved(2)
pg.mixer.set_num_channels(1000)

pg.mixer.music.set_volume(0.4)
pg.mixer.music.load('game/resources/sfx/music.ogg')
pg.mixer.music.play(loops=-1, fade_ms=1000)

pg.mixer.music.set_volume(0.4)