import asyncio

from menu.menu import menu
from util.prepare import initialize
from game.game import game
from util.screens import Screens


async def main():
  initialize()
  screen = Screens.MENU
  while True:
    match screen:
      case Screens.MENU:
        screen = await menu()
      case Screens.GAME:
        screen = await game()


asyncio.run(main())
