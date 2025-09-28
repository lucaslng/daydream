import pygame as pg
import os
import time
from util.prepare import SURF, WINDOW


class HUDSystem:
	def __init__(self):
		self.start_time = time.time()
		self.paused_time = 0.0
		self.is_paused = False
		self.pause_start_time = 0.0
		
		try:
			script_dir = os.path.dirname(os.path.abspath(__file__))
			font_path = os.path.join(script_dir, "..", "..", "..", "menu", "resources", "fonts", "LowresPixel-Regular.otf")
			self.font = pg.font.Font(font_path, 20)
		except:
			self.font = pg.font.SysFont("arial", 18, bold=True)
	
	def pause_timer(self):
		if not self.is_paused:
			self.is_paused = True
			self.pause_start_time = time.time()
	
	def resume_timer(self):
		if self.is_paused:
			self.is_paused = False
			self.paused_time += time.time() - self.pause_start_time
	
	def get_elapsed_time(self) -> float:
		if self.is_paused:
			return self.pause_start_time - self.start_time - self.paused_time
		else:
			return time.time() - self.start_time - self.paused_time
	
	def format_time(self, seconds: float) -> str:
		minutes = int(seconds // 60)
		seconds = seconds % 60
		return f"{minutes:02d}:{seconds:05.2f}"
	
	def draw_shadow_text(self, text: str, x: int, y: int, color=(255, 255, 255)):
		shadow = self.font.render(text, True, (0, 0, 0))
		main = self.font.render(text, True, color)
		
		SURF.blit(shadow, (x + 1, y + 1))
		SURF.blit(main, (x, y))
	
	def render(self, kill_count: int):
		screen_width = WINDOW[0]
		screen_height = WINDOW[1]
		
		x_pos = screen_width - 200
		y_pos = screen_height // 2 - 40

		elapsed_time = self.get_elapsed_time()
		time_text = f"Time: {self.format_time(elapsed_time)}"
		self.draw_shadow_text(time_text, x_pos, y_pos)

		kill_text = f"Kills: {kill_count}"
		self.draw_shadow_text(kill_text, x_pos, y_pos + 30)
