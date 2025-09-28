import asyncio

from menu.menu import menu
from util.prepare import initialize
from game.game import game
from util.screens import Screens
from menu.windows.gameover.gameover import gameover
from menu.windows.levelcomplete.levelclear import levelclear
from menu.windows.ingamemenu.ingamemenu import ingamemenu


async def main():
  initialize()
  screen = Screens.MENU
  while True:
    match screen:
      case Screens.MENU:
        screen = await menu()
      case Screens.GAME:
        screen = await game()
      case Screens.INGAMEMENU:
        screen = await ingamemenu()
      case Screens.GAMEOVER:
        screen = await gameover()
      case Screens.LEVELCLEAR:
        screen = await levelclear()


asyncio.run(main())
