import pyautogui as pag
import numpy as np

colors = {}
def create_color(_name, _r, _g, _b):
    colors[_name] = (_r, _g, _b)
create_color("black", 0, 0, 0)
create_color("white", 255, 255, 255)
create_color("vscodebg", 39, 40, 34)
create_color("cannon_mine", 0, 178, 255)
create_color("mine_bullet", 0, 178, 255)
#create_color("enemy", 241, 78, 84)
#create_color("enemy_bullet", 241, 78, 84)
create_color("cano", 153, 153, 153)
#create_color("shape_square", 255, 232, 105)
#create_color("shape_triangle", 252, 118, 119)
#create_color("shape_pentagon", 118, 141, 252)

class mapColorElement:
    def __init__(self):
        self.elements = {}
        self.colors = {}
    def add(self, _class_name, _color_rgb):
        self.elements[_color_rgb] = _class_name
        self.colors[_class_name] = _color_rgb
    def get_element(self, _color):
        if _color in self.elements:
            return self.elements[_color]
        else:
            return -1
    def get_color(self, _element_name):
        if _element_name in self.colors:
            return self.colors[_element_name]
        else:
            return -1

map_color_element = mapColorElement()
#map_color_element.add("cannon_mine", (0, 178, 255))
#map_color_element.add("mine_bullet", (0, 178, 255))
map_color_element.add("enemy", (241, 78, 84))
map_color_element.add("enemy_bullet", (241, 78, 84))
map_color_element.add("shape_square", (255, 232, 105))
map_color_element.add("shape_triangle", (252, 118, 119))
map_color_element.add("shape_pentagon", (118, 141, 252))


def find_pixel_by_color_polar(_color_name, _x, _y, _dist_min, _dist_max, _params={"step_ang": 1, "step_dist": 1}):
    #for(dist, angle) in np.ndindex(_dist_max-_dist_min, _angle_max):
    for dist in range(_dist_min, _dist_max+_params["step_dist"], _params["step_dist"]):
        for ang in range(0, 360, _params["step_ang"]):

            cos = np.cos(np.deg2rad(ang))
            dx = cos * dist
            sin = np.sin(np.deg2rad(ang))
            dy = sin * dist
            x = int(_x + dx)
            y = int(_y + dy)
            
            print(f"{dx} {dy}")
            if pag.pixelMatchesColor(x, y, colors[_color_name], tolerance=5):
                return (x, y)
