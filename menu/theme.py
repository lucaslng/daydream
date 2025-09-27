import os

def gametheme():
    # Get the directory of this script and construct the font path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(script_dir, "resources", "fonts", "LowresPixel-Regular.otf")
    
    return {
        "@button": {
            "colours": {
                "normal_bg": "#8B0000",      
                "hovered_bg": "#B22222",     
                "active_bg": "#DC143C",      
                "normal_border": "#FF0000",  
                "hovered_border": "#FF4500", 
                "active_border": "#FF6347",  
                "normal_text": "#FFFFFF",   
                "hovered_text": "#FFFFFF",   
                "active_text": "#FFFFFF"     
            },
            "font": {
                "name": "freesansbold.ttf",
                "size": 16,
                "bold": True
            },
            "shape": "rounded_rectangle",
            "shape_corner_radius": 5,
            "border_width": 2
        },
        "@label": {
            "colours": {
                "normal_text": "#FF0000",    
                "normal_bg": "#000000"      
            },
            "font": {
                "name": font_path,
                "size": 21, 
                "bold": True  
}
        }
    }
