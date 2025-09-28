import asyncio

from menu.menu import menu
from util.prepare import initialize
from game.game import game
from util.screens import Screens
from menu.windows.gameover.gameover import gameover
from menu.windows.levelcomplete.levelclear import levelclear
from menu.windows.ingamemenu.ingamemenu import ingamemenu
from menu.windows.finalsummary.finalsummary import finalsummary


async def main():
  initialize()
  screen = Screens.MENU
  level_system = None
  while True:
    match screen:
      case Screens.MENU:
        screen = await menu()
      case Screens.GAME:
        result = await game(level_system)
        if isinstance(result, tuple):
          screen, level_system = result
        else:
          screen = result
      case Screens.INGAMEMENU:
        screen = await ingamemenu()
      case Screens.GAMEOVER:
        screen = await gameover()
      case Screens.LEVELCLEAR:
        screen = await levelclear(level_system)
      case Screens.FINALSUMMARY:
        screen = await finalsummary(level_system)


asyncio.run(main())
