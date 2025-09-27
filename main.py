import asyncio
import pygame

from util.prepare import FPS

pygame.init()
pygame.display.set_mode((320, 240))
clock = pygame.time.Clock()


async def main():
    while True:
        
        pygame.display.update()
        await asyncio.sleep(0)  # You must include this statement in your main loop. Keep the argument at 0.
        clock.tick(FPS)

asyncio.run(main())