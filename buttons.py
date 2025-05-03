import pyautogui as pag

screenW, screenH = pag.size()

btncoords = {
    "play": {"x": screenW/2, "y": screenH-120}
}

def move_and_click(_btn):
    _coords = btncoords[_btn]
    pag.moveTo(_coords["x"], _coords["y"], duration=0.5)
    pag.click()



