
from colors import*

import json



with open("default.json", "r") as f:
    defaultInfo = json.load(f)



undentified_elements = []

class element:
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        self.radius = _radius
        self.type = self#"element"
    stalk_list = None
    ##stalk_list = manager.list() # bullets, enemies, etc i still need to identify
    #color = colors["enemy"] # enemy, enemy_bullet, etc
    #def check_is_me(self, _element):
    #    return abs(self.radius - _element["radius"]) <= 1
class element_undefined(element):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        self.type = self#"element_undefined"
    #stalk_list = manager.list() # bullets, enemies, etc i still need to identify
class element_danger(element_undefined):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        self.radius = _radius
        self.type = self#"element_danger"
    ##stalk_list = manager.list() # bullets, enemies, etc i still need to identify
    #color = colors["enemy"] # enemy, enemy_bullet, etc
    def identify(self):
        print(f"type {self.type}")
        if self.radius > defaultInfo["radius"]["cannon"] - 2:
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
    #stalk_list = manager.list() # bullets, enemies, etc i still need to identify
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
    #stalk_list = manager.list()
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
    #stalk_list = manager.list() # bullets, enemies, etc i still need to identify
    #color = colors["enemy"] # enemy, enemy_bullet, etc
class shape_square(shape):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        #self.radius = _radius
        self.type = self#"shape_square"
    #stalk_list = manager.list() # bullets, enemies, etc i still need to identify
    #color = colors["shape_square"] # enemy, enemy_bullet, etc
class shape_triangle(shape):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        #self.radius = _radius
        self.type = self#"shape_square"
    #stalk_list = manager.list() # bullets, enemies, etc i still need to identify
    #color = colors["shape_triangle"] # enemy, enemy_bullet, etc
class shape_pentagon(shape):
    def __init__(self, _x, _y, _radius):
        self.x = _x
        self.y = _y
        #self.radius = _radius
        self.type = self#"shape_square"
    #stalk_list = manager.list() # bullets, enemies, etc i still need to identify
    #color = colors["shape_pentagon"] # enemy, enemy_bullet, etc


def get_all_subclasses(_class):
    subclasses = []
    for subclass in _class.__subclasses__():
        subclasses.append(subclass)
        subclasses.extend(get_all_subclasses(subclass))
    return subclasses

def get_all_headclasses(_class):
    all_classes = get_all_subclasses(element)
    final_classes = [cls for cls in all_classes if not cls.__subclasses__()]
    return final_classes


def str_to_element_class(_str):
    return globals().get(_str)


from multiprocess import get_manager
def init_element_lists():
    for headclass in get_all_headclasses(element):
        manager = get_manager()
        headclass.stalk_list = manager.list()