import asyncio
import pygame

from menu.menu import menu
from game.game import game
from util.prepare import initialize
from util.screens import Screens


async def main():
  initialize()
  screen = Screens.MENU
  while True:
    match screen:
      case Screens.MENU:
        state = await menu()
      case Screens.GAME:
        state = await game()


asyncio.run(main())
