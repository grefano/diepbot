import pyautogui as pag


from vision import*
from vigilate import*



def identify_element(_element):
    print(f"type {_element.type}")
    if _element.type == "element_danger":
        # verificar TAMANHO e bullet TEM CANHAO
        if _element.radius > default_cannon_radius-2:
            return "enemy"
        else:
            return "enemy_bullet"

    return False

def categorize_element(_element):
    identity = identify_element(_element)
    if identity == False:
        return False
    
    if identity == "enemy":
        stalking_enemies.append(_element)
        stalking_enemies[-1].type = "enemy"
        print(f"tem raio {_element.radius}, é canhao inimigo")
    elif identity == "enemy_bullet":
        enemy_bullets.append(_element)
        enemy_bullets[-1].type = "enemy_bullet"
        print(f"tem raio {_element.radius}, é tiro inimigo")


def identify_elements():
    #indentifed_indexes = []
    e = 0
    size = stalking_elements.__len__()
    while e < size:
        categorized = categorize_element(stalk_elements[e])
        if categorized:
            #indentifed_indexes.append(e)
            stalking_elements.pop(e)
            e-=1
            size-=1
        e+=1




def compare_enemy_element(_enemy, _element):
    print(f"compare enemy {_enemy.radius} element {_element["radius"]}")
    if _element["radius"] < _enemy.radius:
        return False

    if _enemy.radius == _element["radius"]:
        return True
    else:
        return False

def compare_bullet_element(_bullet, _element):
    print(f"compare bullet {_bullet.radius} element {_element["radius"]}")
    if _bullet.radius == _element["radius"]:
        return True
    else:
        return False


def stalk_elements():
    for e in range(0, stalking_enemies.__len__()):
        distmax = default_cannon_radius*2*4
        for dist in range(0, distmax, 12):
            for ang in range(0, 360, 10):
                x, y = get_polar_coords(stalking_enemies[e].x, stalking_enemies[e].y, dist, ang)
                pag.moveTo(x, y)
                
                #print(f"stalking enemy {x} {y}")
                element = pag.pixelMatchesColor(x, y, colors["enemy"], tolerance=5)
                if element:    
                    print(f"stalking enemies, enemy at {x} {y}")
                    info = get_element_spacial_info(x, y)
                    isSame = compare_enemy_element(stalking_enemies[e], info)
                    pag.moveTo(stalking_enemies[e].x, stalking_enemies[e].y, duration=0.0)
                    print(f"is same {isSame}")
                    if isSame:
                        pag.moveTo(info["x"], info["y"], duration=1.0)

    for b in range(0, enemy_bullets.__len__()):
        distmax = default_bullet_radius*2*4
        for dist in range(0, distmax, 12):
            for ang in range(0, 360, 10):
                x, y = get_polar_coords(enemy_bullets[b].x, enemy_bullets[b].y, dist, ang)
                pag.moveTo(x, y)
                
                #print(f"stalking enemy {x} {y}")
                element = pag.pixelMatchesColor(x, y, colors["enemy"], tolerance=5)
                if element:    
                    print(f"stalking bullets, bullet at {x} {y}")
                    info = get_element_spacial_info(x, y)
                    isSame = compare_bullet_element(enemy_bullets[b], info)
                    pag.moveTo(enemy_bullets[b].x, enemy_bullets[b].y, duration=0.0)
                    print(f"is same {isSame}")
                    if isSame:
                        pag.moveTo(info["x"], info["y"], duration=1.0)

