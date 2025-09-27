import asyncio
import pygame as pg

from util.prepare import CLOCK, FPS

async def update_screen() -> float:
	time_delta = CLOCK.tick(FPS) / 1000.0
	pg.display.update() # try flip later
	await asyncio.sleep(0)
	return time_delta