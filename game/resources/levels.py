
from dataclasses import dataclass
from enum import Enum, auto


class DoorDirections(Enum):
  V = auto()
  H = auto()


@dataclass
class EnemyInfo():
  pos: tuple[int, int]


class DoorInfo():
  pos: tuple[int, int]
  direction: DoorDirections


@dataclass
class Level():
  enemies: list[EnemyInfo]
  doors: list[DoorInfo]


LEVELS: list[Level] = [
    Level([
        EnemyInfo((500, 400)),
        EnemyInfo((800, 600)),
        EnemyInfo((1200, 800)),
    ],
        [])
]
