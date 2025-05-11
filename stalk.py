#import pyautogui as pag


#from vision import*
from look import*



def identify_element(_element):
    
    return _element.identify()

def categorize_element(_element):
    identity = identify_element(_element)
    print(f"identity {identity}")
    if identity == False:
        return False
    

    identity.stalk_list.append(identity(_element.x, _element.y, _element.radius))
    #identity.stalk_list[-1].type = identity
    print(f"tem raio {_element.radius}, é {identity.__name__}")
    return True


def identify_elements():
    #indentifed_indexes = []
    e = 0
    size = undentified_elements.__len__()
    while e < size:
        categorized = categorize_element(undentified_elements.stalk_list[e])
        if categorized:
            #indentifed_indexes.append(e)
            undentified_elements.stalk_list.pop(e)
            e-=1
            size-=1
        e+=1




def stalk_elements():
    stalk(enemy)
    stalk(enemy_bullet)

def stalk(_class):
    #for b in range(0, _class.stalk_list.__len__()):
    for element in _class.stalk_list:
        distmax = defaultInfo["radius"]["bullet"]*2*4
        for dist in range(0, distmax, 12):
            for ang in range(0, 360, 10):
                x, y = get_polar_coords(element.x, element.y, dist, ang)
                pag.moveTo(x, y)
                
                color = map_color_element.get_color(_class)
                here = pag.pixelMatchesColor(x, y, color, tolerance=5)
                if here:    
                    print(f"stalking {_class.__name__}, one at {x} {y}")
                    info = get_element_spacial_info(x, y, color)
                    isSame = element.check_is_me(info)
                    #isSame = compare_bullet_element(_class.stalk_list[b], info)
                    pag.moveTo(element.x, element.y, duration=0.0)
                    print(f"is same {isSame}, {_class.__name__}")
                    if isSame:
                        pag.moveTo(info["x"], info["y"], duration=1.0)
                        return True
    return False    
