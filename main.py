import asyncio

from menu.menu import menu
from util.prepare import initialize
from game.game import game
from util.screens import Screens
from menu.resources.gameover.gameover import gameover



async def main():
  initialize()
  screen = Screens.MENU
  while True:
    match screen:
      case Screens.MENU:
        screen = await menu()
      case Screens.GAME:
        screen = await game()
      case Screens.GAMEOVER:
        screen = await gameover()


asyncio.run(main())
