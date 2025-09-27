
from typing import Protocol

from game.ecs.Entity import Entity


class System(Protocol):

	def __init__(self): ...

	def update(self, entities: list[Entity], dt: int): ...
	