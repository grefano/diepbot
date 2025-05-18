
import pyautogui as pag
import time
import numpy as np
from multiprocessing import Process

from buttons import* 
from colors import*
from multiprocess import get_manager, init_manager

from menu import*

from default_info import*
from stalk import*

pag.FAILSAFE = False


shutdown_flag = False

def collect_info():
    global shutdown_flag
    while not shutdown_flag:
        #print("get info")
        look_screen_borders(look_element_check)

        identify_elements()
        for e in range(0, undentified_elements.__len__()):
            print(f"stalkel radius{undentified_elements[e].radius}")
        for e in range(0, enemy.stalk_list.__len__()):
            print(f"enemy radius {enemy.stalk_list[e].radius}")
        for e in range(0, enemy_bullet.stalk_list.__len__()):
            print(f"bullet radius {enemy_bullet.stalk_list[e].radius}")

        stalk_elements()


def act():
    # atirar inimigos
    # buscar formas
    # mover
    #blalblab
    global shutdown_flag
    while not shutdown_flag:
        for e in enemy.stalk_list:
            print(f"ir para {e["x"]} {e["y"]}")

            pag.moveTo(e["x"], e["y"], 0.5)


if __name__ == "__main__":
    #move_and_click("retry")
    #move_and_click("play")
    #init_manager()
    init_manager()
    init_element_lists()

    manager = get_manager()
    set_gamescreen()
    print(gamescreen.__str__())
    #pag.moveTo(gamescreen.gameX, gamescreen.gameY, 0.5)
    #pag.moveTo(gamescreen["x"], gamescreen["y"], 0.5)

    
    print(f"started processes")

    pVision = Process(target=collect_info)
    #pAct = Process(target=act)

    pVision.start()
    #pAct.start()

    pVision.join()
    #pAct.join()

while False:
    if reset_default_info:
        print(f"set default info")
        set_default_info()
        continue

    print(f"nao resetou default info")
    update_elements()

    stalk_elements()

    continue


