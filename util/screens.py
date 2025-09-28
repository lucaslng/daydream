from enum import Enum, auto


class Screens(Enum):
	MENU = auto()
	GAME = auto()
	INGAMEMENU = auto()
	GAMEOVER = auto()
	LEVELCLEAR = auto()
	FINALSUMMARY = auto()
	DEADMESSAGE = auto()