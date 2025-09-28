import pygame
import os
from datetime import datetime

def save_screenshot(surface, filename_prefix="screenshot"):
    try:
        os.makedirs("dump/temp", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"dump/temp/{filename_prefix}_{timestamp}.png"
        pygame.image.save(surface, filename)
        return filename
    except Exception as e:
        print(f"cant screenshot{e}")
        return None
