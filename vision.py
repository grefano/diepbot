# IN-GAME vision related code
print(f"vision name {__name__}")
#if __name__ == '__main__':
import pyautogui as pag

from elements import*
import numpy as np

gamescreen = {}
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
    while pag.pixelMatchesColor(xleft, _y, _color, tolerance=5):
        xleft -= 1

    xright  = _x
    while pag.pixelMatchesColor(xright, _y, _color, tolerance=5):
        xright += 1

    ytop = _y
    while pag.pixelMatchesColor(_x, ytop, _color, tolerance=5):
        ytop -= 1

    ybottom = _y
    while pag.pixelMatchesColor(_x, ybottom, _color, tolerance=5):
        ybottom += 1
    
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

class game_screen:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.gameX = 0
        self.gameY = 0
    def __str__(self):
        return f"x {self.x} y {self.y} width {self.width} height {self.height} gamex {self.gameX} gamey {self.gameY}"
gamescreen = game_screen()

def set_gamescreen():
    for dist in range(1, 60, 15):
        for ang in range(0, 360, 10):
            x, y = get_polar_coords(int(screenW/2), int(screenH/2), dist, ang)
            pag.moveTo(x,y,0.0)
            print(f" {pag.pixel(x, y)} {colors["cannon_mine"]}")
            if pag.pixelMatchesColor(x, y, colors["cannon_mine"], tolerance=5):
                print("matches")
                info = get_element_spacial_info(x, y, colors["cannon_mine"])
                pag.moveTo(x, y, 0.5)


                cannonYOfs = info["y"]-screenH/2
                #global gamescreen
                gamescreen.x = 0
                gamescreen.y = int(cannonYOfs*2)
                gamescreen.width = int(screenW)
                gamescreen.height = int(screenH-cannonYOfs*2)
                gamescreen.gameX = int(gamescreen.x + gamescreen.width/2)
                gamescreen.gameY = int(gamescreen.y + gamescreen.height/2)
                
                

                

                return




def element_stalk(_x, _y, _class):
    # ja sabe que tem alguma coisa vermelha aqui
    # definindo dimensoes do objeto
    
    info = get_element_spacial_info(_x, _y, map_color_element.get_color(_class.__name__))
    #element_danger.stalk_list.append(element_danger(info["x"], info["y"], info["radius"]))

    undentified_elements.append(_class(info["x"], info["y"], info["radius"]))

        

