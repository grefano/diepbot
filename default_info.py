if __name__ == '__main__':

    from look import*

    reset_default_info = False


    def json_key_exists(_json, _keys):
        current = _json
        for key in _keys:
            if key in current:
                current = current[key]
            else:
                return False
        return True



    if reset_default_info:
        with open("default.json", "w") as f:
            json.dump({}, f)


            #if foundme == False:
            #    done = False


    def set_default_info():
        # own cannon radius, bullet (smaller red circle)
        #print(f"bosta: {defaultInfo["adwoijawd"]}")
        done = True
        
        if not json_key_exists(defaultInfo, ['radius', 'cannon']):
            if pag.pixelMatchesColor(gamescreen["gameX"], gamescreen["gameY"], colors["cannon_mine"], tolerance=5):  
                me = get_element_spacial_info(gamescreen["gameX"], gamescreen["gameY"], colors["cannon_mine"])
                defaultInfo["radius"] = {}
                defaultInfo["radius"]["cannon"] = me["radius"]
            else:
                done = False
                
        #print(f"set default info")
        if not json_key_exists(defaultInfo, ['radius', 'bullet']):
            print(f"key radius bullet not found")
            #move_and_click(screenW/2, screenH/2, 0.0)
            #pag.moveTo(int(screenW/2), int(screenH/2), duration=0.0)
            bullets = look_screen_borders(
                lambda x, y: pag.pixelMatchesColor(x, y, map_color_element.get_color("enemy_bullet"), tolerance=5)
            )
            if bullets.__len__() > 0:
                print(f"FOUND BULLET")
                info = get_element_spacial_info(bullets[0]["xfound"], bullets[0]["yfound"], colors["mine_bullet"])
                pag.moveTo(info["x"], info["y"], duration=1.0)
                defaultInfo["radius"] = {}
                defaultInfo["radius"]["bullet"] = info["radius"]
            else:
                done = False
        if done:
            with open("default.json", "w") as f:
                json.dump(defaultInfo, f)

