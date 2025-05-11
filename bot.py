import pyautogui as pag
import time
import numpy as np

from buttons import* 
from colors import*

from menu import*

from default_info import*
from stalk import*

pag.FAILSAFE = False




def update_elements():
    # vigiar bordas da tela e vigiar posições proximas aos elementos
    look_screen_borders(look_element_check)

    identify_elements()
    for e in range(0, undentified_elements.__len__()):
        print(f"stalkel radius{undentified_elements[e].radius}")
    for e in range(0, enemy.stalk_list.__len__()):
        print(f"enemy radius {enemy.stalk_list[e].radius}")
    for e in range(0, enemy_bullet.stalk_list.__len__()):
        print(f"bullet radius {enemy_bullet.stalk_list[e].radius}")




#move_and_click("retry")
move_and_click("play")

set_gamescreen()

print(gamescreen.__str__())
pag.moveTo(gamescreen.gameX, gamescreen.gameY, 0.5)
#pag.moveTo(gamescreen["x"], gamescreen["y"], 0.5)

while True:
    if reset_default_info:
        print(f"set default info")
        set_default_info()
        continue

    print(f"nao resetou default info")
    update_elements()

    stalk_elements()

    continue


