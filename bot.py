import pyautogui as pag
import time
import numpy as np

from buttons import* 
from colors import*

from menu import*

from vision import*
from vigilate import*
from stalk import*

pag.FAILSAFE = False

def json_key_exists(_json, _keys):
    current = _json
    for key in _keys:
        if key in current:
            current = current[key]
        else:
            return False
    return True


reset_default_info = True
if reset_default_info:
    with open("default_info.json", "w") as f:
        json.dump({}, f)

def set_default_info():
    # own cannon radius, bullet (smaller red circle)
    with open("default_info.json", "r") as f:
        default_info = json.load(f)
    #print(f"bosta: {default_info["adwoijawd"]}")
    if not json_key_exists(default_info, ['radius', 'cannon']) and pag.pixelMatchesColor(int(screenW/2), int(screenH/2), colors["cannon_mine"], tolerance=5):  
        me = get_element_spacial_info(int(screenW/2), int(screenH/2), colors["cannon_mine"])
        default_info["radius"]["cannon"] = me["radius"]

    print(f"set default info")
    if not json_key_exists(default_info, ['radius', 'bullet']):
        print(f"key radius bullet not found")
        #move_and_click(screenW/2, screenH/2, 0.0)
        pag.moveTo(int(screenW/2), int(screenH/2), duration=0.0)
        bullets = look_screen_borders(
            lambda x, y: pag.pixelMatchesColor(x, y, colors["enemy_bullet"], tolerance=5)
        )
        if bullets.__len__() > 0:
            print(f"bullet found")
            info = get_element_spacial_info(bullets[0]["xfound"], bullets[0]["yfound"], colors["mine_bullet"])
            pag.moveTo(info["x"], info["y"], duration=1.0)
            default_info["radius"]["bullet"] = info["radius"]
    
    with open("default_info.json", "w") as f:
        json.dump(default_info, f)

def update_elements():
    # vigiar bordas da tela e vigiar posições proximas aos elementos
    look_screen_borders(vigilate_check)

    identify_elements()

    for e in range(0, undentified_elements.__len__()):
        print(f"stalkel radius{undentified_elements[e].radius}")
    for e in range(0, enemy.stalk_list.__len__()):
        print(f"enemy radius {enemy.stalk_list[e].radius}")
    for e in range(0, enemy_bullet.stalk_list.__len__()):
        print(f"bullet radius {enemy_bullet.stalk_list[e].radius}")

    

while True:
    if reset_default_info:
        set_default_info()
        continue
    
    update_elements()

    stalk_elements()

    continue


