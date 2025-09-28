from pygame import Sound


def soundFactory(fileName: str, volume: float=0.6) -> Sound:
	sound = Sound(f'game/resources/sfx/{fileName}.ogg')
	sound.set_volume(volume)
	return sound

boom_sound = soundFactory("boom")