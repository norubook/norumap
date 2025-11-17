
color_code={
    'w':(255,255,255,255),
    'r':(255,0,0,255),
    'g':(0,255,0,255),
    'b':(0,0,255,255),
    'n':(0,0,0,0)
}


    #モード
modes ={
    "input_save": False,
    "input_load" : False,
    "position" : False,
    "limited_save" :False,
    "hierarchy": False,
}

def all_mode_off(modes):
    for key in modes:
        modes[key] = False