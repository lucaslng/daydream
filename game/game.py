from game.ecs.Entity import Entity
from util.screens import Screens
from util.update_screen import update_screen


async def game() -> Screens:
	# entities: list[Entity]
	while True:
		await update_screen()