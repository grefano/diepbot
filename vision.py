# IN-GAME vision related code

import pyautogui as pag

from elements import*




screenW, screenH = pag.size()

def get_polar_coords(_x, _y, _dist, _ang):
    cos = np.cos(np.deg2rad(_ang))
    dx = cos * _dist
    sin = np.sin(np.deg2rad(_ang))
    dy = sin * _dist
    x = int(_x + dx)
    y = int(_y + dy)
    x = max(min(x, screenW-1), 0)
    y = max(min(y, screenH-1), 0)
    return (x, y)

def get_element_dimensions_from_point(_x, _y, _color):
    xleft = _x
    #pag.moveTo(screenW/2, screenH/2, duration=0.0)
    #pag.moveTo(xleft, _y, duration=1.0)
    #print(f"xleft: {xleft} y: {_y}")
    #print(f"xleft enemy: {pag.pixelMatchesColor(xleft, _y, _color, tolerance=5)}")
    #print(f"color: {pag.pixel(xleft, _y)}")
    while pag.pixelMatchesColor(xleft, _y, _color, tolerance=5):
        xleft -= 1
        #print(f"xleft: {xleft}")
        #pag.moveTo(xleft, _y, duration=0.0)

    xright  = _x
    #pag.moveTo(screenW/2, screenH/2, duration=0.0)
    #pag.moveTo(xright, _y, duration=1.0)

    while pag.pixelMatchesColor(xright, _y, _color, tolerance=5):
        xright += 1
        #print(f"xright: {xright}")
        #pag.moveTo(xright, _y, duration=0.0)

    ytop = _y
    #pag.moveTo(screenW/2, screenH/2, duration=0.0)
    #pag.moveTo(_x, ytop, duration=1.0)
    while pag.pixelMatchesColor(_x, ytop, _color, tolerance=5):
        ytop -= 1
        #print(f"ytop: {ytop}")
        #pag.moveTo(_x, ytop, duration=0.0)

    ybottom = _y
    #pag.moveTo(screenW/2, screenH/2, duration=0.0)
    #pag.moveTo(_x, ybottom, duration=1.0)
    while pag.pixelMatchesColor(_x, ybottom, _color, tolerance=5):
        ybottom += 1
        #print(f"ybottom: {ybottom}")
        #pag.moveTo(_x, ybottom, duration=0.0)
    
    return {"xleft": xleft, "ytop": ytop, "xright": xright, "ybottom": ybottom}

def get_element_spacial_info(_x, _y, _color):
    posmax = get_element_dimensions_from_point(_x, _y, _color)
    #print(f"color enemy: {colors["enemy"]}")
    #print(f"posmax: {posmax}")
    #print(f"cor 5: {pag.pixel(5, 5)}")

    diffw = (posmax["xright"]-_x)-(_x-posmax["xleft"])
    diffh = (posmax["ybottom"]-_y)-(_y-posmax["ytop"])

    xcenter = int(_x + diffw/2)
    ycenter = int(_y + diffh/2)
    pag.moveTo(xcenter, ycenter, duration=1.0)

    # descobrindo raio real

    #print(f"X: {posmax["xleft"]} Y: {posmax["ytop"]} X: {posmax["xright"]} Y: {posmax["ybottom"]}")
    #print(f"X: {xcenter} Y: {ycenter}")
    raio = int(max(posmax["xright"]-posmax["xleft"], posmax["ybottom"]-posmax["ytop"])/2)
    #print(f"Raio errado: {raio}")
    y = ycenter - raio
    while pag.pixelMatchesColor(xcenter, y, _color, tolerance=5):
        y -= 1
    #print(f"_y {_y} y {y}")
    raio = ycenter-y
    pag.moveTo(xcenter, y, duration=0.0)    

    #print(f"Raio: {raio}")

    return {"x": xcenter, "y": ycenter, "radius": raio}

def element_stalk(_x, _y, _class):
    # ja sabe que tem alguma coisa vermelha aqui
    # definindo dimensoes do objeto
    
    info = get_element_spacial_info(_x, _y, _class.color)
    #element_danger.stalk_list.append(element_danger(info["x"], info["y"], info["radius"]))

    undentified_elements.append(_class(info["x"], info["y"], info["radius"]))

        

