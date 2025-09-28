
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
  spawn_pos: tuple[int, int]
  enemies: list[EnemyInfo]
  doors: list[DoorInfo]


LEVELS: list[Level] = [
    Level(
      (514, 1704),
      [
        EnemyInfo((576, 1243)),
        EnemyInfo((384, 739)),
        EnemyInfo((656, 514)),
        EnemyInfo((1017, 354)),
        EnemyInfo((1155, 916)),
        EnemyInfo((1122, 1685)),
        EnemyInfo((1674, 988)),
        EnemyInfo((1714, 492)),
          ],
        []),
    Level(
        (1032, 737),
        [
            EnemyInfo((1383, 745)),
            EnemyInfo((1774, 1250)),
            EnemyInfo((533, 810)),
            EnemyInfo((308, 1691)),
            EnemyInfo((308, 1827)),
            EnemyInfo((476, 1691)),
            EnemyInfo((476, 1827)),
            EnemyInfo((1767, 1691)),
            EnemyInfo((1767, 1827)),
            EnemyInfo((1623, 1691)),
            EnemyInfo((1623, 1827)),
        ], []),
    Level(
        (1028, 1931),
        [
            EnemyInfo((627, 762)),
            EnemyInfo((322, 529)),
            EnemyInfo((963, 408)),
            EnemyInfo((1779, 535)),
            EnemyInfo((1394, 735)),
            EnemyInfo((993, 328)),
        ], [])
]
