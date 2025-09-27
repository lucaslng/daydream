import asyncio
import pygame as pg

from util.prepare import CLOCK, FPS

async def update_screen() -> None:
	pg.display.update() # try flip later
	await asyncio.sleep(0)
	CLOCK.tick(FPS)