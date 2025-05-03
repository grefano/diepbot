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

def update_elements():
    # vigiar bordas da tela e vigiar posições proximas aos elementos
    vigilate_screen_borders()

    identify_elements()

    for e in range(0, stalking_elements.__len__()):
        print(f"stalkel radius{stalking_elements[e].radius}")
    for e in range(0, stalking_enemies.__len__()):
        print(f"enemy radius {stalking_enemies[e].radius}")
    for e in range(0, enemy_bullets.__len__()):
        print(f"bullet radius {enemy_bullets[e].radius}")

    stalk_elements()

update_elements()

