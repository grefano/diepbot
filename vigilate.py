import pyautogui as pag

from buttons import*
from colors import*

from vision import*

def is_checking_defined_element(_x, _y): # verifica se o elemento que ta sendo verificado já foi adicionado a lista de elementos
    for element in element_danger.stalk_list:
        if _x >= element.x - element.radius and _x <= element.x + element.radius and _y >= element.y - element.radius and _y <= element.y + element.radius:
            return True
    return False

def vigilate_check(_x, _y):
    #print(f"checking {_x} {_y}")
    if is_checking_defined_element(_x, _y):
        print(f"already checked {_x} {_y}")
        return True

    element = pag.pixelMatchesColor(_x, _y, element_danger.color, tolerance=5)
    if element:
        print(f"\n enemy at {_x} {_y}")
        pag.moveTo(_x, _y, duration=0.0)
        element_stalk(_x, _y)
        return True
    else:
        return False

def vigilate_screen_borders():
    border = 100
    diststep = 12

    for hside in range(-1, 2, 2):
        xmax = int(screenW/2 + hside*screenW/2)
        for x in range(xmax, xmax - hside*border, -hside*diststep):
            x = min(x, screenW-1)
            for y in range(0, screenH, diststep):
                #print(f"X: {x} Y: {y} side {hside}")
                #pag.moveTo(x, y, duration=0.0)
                vigilate_check(x, y)
                if hside == 1:
                    continue

    return True

    for vside in range(-1, 2, 2):
        ymax = int(screenH/2 + vside*screenH/2)
        for y in range(ymax, ymax - vside*border, -vside*diststep):
            y = min(y, screenH-1)
            for x in range(0, screenW, diststep):                
                #print(f"Y: {y} X: {x}")
                
                vigilate_check(x, y)


def vigilate_mouse_polar():
    mousepos = pag.position()
    for dist in range(1, 60, 15):
        for ang in range(0, 360, 10):
            x, y = get_polar_coords(mousepos.x, mousepos.y, dist, ang)
            #print(f"dist: {dist} ang: {ang}")
            vigilate_check(x, y)
