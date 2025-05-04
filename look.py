# LOOK DANGER ELEMENTS (ENEMIES AND BULLETS)

import pyautogui as pag

#from buttons import*
#from colors import*



from vision import*


#def is_checking_defined_element(_x, _y): # verifica se o elemento que ta sendo verificado já foi adicionado a lista de elementos
#    for element in undentified_elements:
#        if _x >= element.x - element.radius and _x <= element.x + element.radius and _y >= element.y - element.radius and _y <= element.y + element.radius:
#            return True
#    return False


def look_screen_borders(_func_check):
    border = 100
    diststep = 12
    elements = []
    for hside in range(-1, 2, 2):
        xmax = int(screenW/2 + hside*screenW/2)
        for x in range(xmax, xmax - hside*border, -hside*diststep):
            x = min(x, screenW-1)
            for y in range(0, screenH, diststep):
                #print(f"X: {x} Y: {y} side {hside}")
                #pag.moveTo(x, y, duration=0.0)
                posfound = {"xfound": x, "yfound": y}
                check = _func_check(x, y) 
                if check != False:
                    posfound.update({"check": check})
                    elements.append(posfound)
                
                #vigilate_check(x, y)

    for vside in range(-1, 2, 2):
        ymax = int(screenH/2 + vside*screenH/2)
        for y in range(ymax, ymax - vside*border, -vside*diststep):
            y = min(y, screenH-1)
            for x in range(0, screenW, diststep):                
                posfound = {"xfound": x, "yfound": y}
                check = _func_check(x, y) 
                if check != False:
                    posfound.update({"check": check})
                    elements.append(posfound)
    return elements


def is_looking_old_element(_x, _y):
    headclasses = get_all_headclasses(element)
    
    for headclass in headclasses:
        color = map_color_element.get_color(headclass.__name__)
        if pag.pixelMatchesColor(_x, _y, color, tolerance=5): 
            for element in headclass.stalk_list:
                info = get_element_spacial_info(_x, _y, color)
                isMe = element.check_is_me(info)
                if isMe:
                    return True
    return False

def look_element_check(_x, _y):
    # preciso saber se esse elemento ja foi olhado
    if is_looking_old_element(_x, _y):
        return False
    
    color = pag.pixel(_x, _y)
    classe = map_color_element.get_class(color)
    if classe.__base__ == element_undefined:
        print(f"lookcheck undefined at {_x} {_y}")
        element_stalk(_x, _y, element_undefined)
    else:
        print(f"lookcheck {classe.__name__} at {_x} {_y}")
        element_stalk(_x, _y, classe)
    
    return True
   

#def vigilate_check(_x, _y):
#    #print(f"checking {_x} {_y}")
#    if is_checking_defined_element(_x, _y):
#        print(f"already checked {_x} {_y}")
#        return True###
#
#    element = pag.pixelMatchesColor(_x, _y, element_danger.color, tolerance=5)
#    if element:
#        print(f"\n enemy at {_x} {_y}")
#        pag.moveTo(_x, _y, duration=0.0)
#        element_stalk(_x, _y, element_danger)
#        return True
#    else:
#        return False

#def vigilate_mouse_polar():
#    mousepos = pag.position()
#    for dist in range(1, 60, 15):
#        for ang in range(0, 360, 10):
#            x, y = get_polar_coords(mousepos.x, mousepos.y, dist, ang)
#            #print(f"dist: {dist} ang: {ang}")
#            vigilate_check(x, y)
