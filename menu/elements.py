from util.prepare import WINDOW

center_x = WINDOW[0] // 2
center_y = WINDOW[1] // 2


def button_configs():
    button_width = 160
    button_height = 35

    return {
        "play": {
            "rect": (center_x - button_width//2, center_y - 20, button_width, button_height),
            "text": "Make metal bleed. . ."
        },
        # "settings": {
        #     "rect": (center_x - button_width//2, center_y + 25, button_width, button_height),
        #     "text": "not needed"
        # },
        "quit": {
            "rect": (center_x - button_width//2, center_y + 30, button_width, button_height),
            "text": "Conserve your flesh. . . "

        }
    }

def label_configs():
    
    return {
        "title": {
            "rect": (center_x - 80, 30, 160, 50),
            "text": "Bleeding Metal",
            "color": (255, 0, 0)
        },
        "title_bleeding": {
            "rect": (center_x - 65, 20, 80, 50),
            "text": "Bleeding",
            "color": (136, 8, 8)
        },
        "title_metal": {
            "rect": (center_x, 30, 40, 50),
            "text": "Metal",
            "color": (67, 70, 75)
        },
        "subtitle": {
            "rect": (center_x - 200, 70, 400, 30),
            "text": "Great power comes with great sacrifice.",
            "color": (255, 255, 255)
        }
    }
