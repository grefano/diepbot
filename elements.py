
from colors import*

import json

with open("default_info.json", "r") as f:
    default_info = json.load(f)



undentified_elements = []

class element:
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        self.radius = _radius
        self.type = self#"element"
    stalk_list = [] # bullets, enemies, etc i still need to identify
    #color = colors["enemy"] # enemy, enemy_bullet, etc
    #def check_is_me(self, _element):
    #    return abs(self.radius - _element["radius"]) <= 1
class element_undefined(element):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        self.type = self#"element_undefined"
    stalk_list = [] # bullets, enemies, etc i still need to identify
class element_danger(element_undefined):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        self.radius = _radius
        self.type = self#"element_danger"
    #stalk_list = [] # bullets, enemies, etc i still need to identify
    #color = colors["enemy"] # enemy, enemy_bullet, etc
    def identify(self):
        print(f"type {self.type}")
        if self.radius > default_info["radius"]["cannon"] - 2:
            return enemy
        else:
            return enemy_bullet

class enemy(element):
    def __init__(self, _x, _y, _radius, _angle=0, _speed=0):
        self.x = _x
        self.y = _y
        self.radius = _radius
        self.angle = _angle
        self.speed = _speed
        self.type = self#"enemy"
    stalk_list = [] # bullets, enemies, etc i still need to identify
    #color = colors["enemy"] # enemy, enemy_bullet, etc
    def check_is_me(self, _element):
        if _element["radius"] < self.radius:
            return False
        return self.radius == _element["radius"]  
class enemy_bullet(element):
    def __init__(self, _x, _y, _radius, _angle=0, _speed=0):
        self.x = _x
        self.y = _y
        self.radius = _radius
        self.angle = _angle
        self.speed = _speed
        self.type = self#"enemy_bullet"
    stalk_list = []
    #color = colors["enemy"] # enemy, enemy_bullet, etc
    def check_is_me(self, _element):
        print(f"is me {self.radius} {_element['radius']}")
        return abs(self.radius - _element["radius"]) <= 1

class shape(element):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        #self.radius = _radius
        self.type = self#"shape"
    stalk_list = [] # bullets, enemies, etc i still need to identify
    #color = colors["enemy"] # enemy, enemy_bullet, etc
class shape_square(shape):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        #self.radius = _radius
        self.type = self#"shape_square"
    stalk_list = [] # bullets, enemies, etc i still need to identify
    #color = colors["shape_square"] # enemy, enemy_bullet, etc
class shape_triangle(shape):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        #self.radius = _radius
        self.type = self#"shape_square"
    stalk_list = [] # bullets, enemies, etc i still need to identify
    #color = colors["shape_triangle"] # enemy, enemy_bullet, etc
class shape_pentagon(shape):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        #self.radius = _radius
        self.type = self#"shape_square"
    stalk_list = [] # bullets, enemies, etc i still need to identify
    #color = colors["shape_pentagon"] # enemy, enemy_bullet, etc


def get_all_headclasses(_class):
    subclasses = _class.__subclasses__()
    heads = [subclass for subclass in subclasses if not subclass.__subclasses__()]
    return heads        
