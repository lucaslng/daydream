from util.prepare import WINDOW


def button_configs():
    button_width = 160
    button_height = 35
    center_x = WINDOW[0] // 2
    center_y = WINDOW[1] // 2
    
    return {
        "play": {
            "rect": (center_x - button_width//2, center_y - 20, button_width, button_height),
            "text": "start tbd"
        },
        "settings": {
            "rect": (center_x - button_width//2, center_y + 25, button_width, button_height),
            "text": "settings - tbd if needed"
        },
        "quit": {
            "rect": (center_x - button_width//2, center_y + 70, button_width, button_height),
            "text": "quit tbd"
        }
    }


def label_configs():
    center_x = WINDOW[0] // 2
    
    return {
        "title": {
            "rect": (center_x - 80, 30, 160, 50),
            "text": "Title Here"
        },
        "subtitle": {
            "rect": (center_x - 140, 70, 280, 30),
            "text": "SACRIFICES MUST BE MADE"
        }
    }
