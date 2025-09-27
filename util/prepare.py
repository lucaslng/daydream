import pygame as pg


FPS = 60
WINDOW = (320, 240)
CLOCK = pg.time.Clock()
SURF = pg.display.set_mode(WINDOW)

def initialize():
	'''initialize program'''
	pg.init()
	pg.event.set_allowed([pg.QUIT, pg.KEYDOWN, pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP])
	pg.font.init()
	# pg.mixer.init()
	# pg.mixer.set_reserved(2)
	# pg.mixer.set_num_channels(1000)
	
	pg.mixer.music.set_volume(0.4)