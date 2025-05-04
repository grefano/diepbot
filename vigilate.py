import pyautogui as pag

#from buttons import*
#from colors import*

from vision import*


def is_checking_defined_element(_x, _y): # verifica se o elemento que ta sendo verificado já foi adicionado a lista de elementos
    for element in undentified_elements:
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
        element_stalk(_x, _y, element_danger)
        return True
    else:
        return False

def vigilate_mouse_polar():
    mousepos = pag.position()
    for dist in range(1, 60, 15):
        for ang in range(0, 360, 10):
            x, y = get_polar_coords(mousepos.x, mousepos.y, dist, ang)
            #print(f"dist: {dist} ang: {ang}")
            vigilate_check(x, y)
