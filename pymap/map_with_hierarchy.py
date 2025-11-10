##変数を用いて書き込みのon,offを行います.
##範囲外の座標を指定して読み取りを行う場合エラーが出るため，上下左右実装後座標を動かしてセーブする予定．
##予めサイズを決めておいた方がいい？
#全体マップ2000*2000
#フロアマップ1000*1000
#フロアマップか全体マップか把握するためにcsv1行目は特殊記号を用いるのが良いかも


'''
現在状況

できたこと
移動した場合のロードやセーブをどうするか(仮置きで全体保存全体ロードとして実装)

任意の場所にロード

任意の場所にロードした場合，もしくは通常サイズより大きいマップをロードした場合，
　はみ出した部分だけ無視する方法

階層表示

できていないこと

拡大縮小

任意の場所をセーブ

(ドット単位でのセーブ)

関連マップをロードした場合，同じ場所を再ロードしないようにする方法．
(サブマップを三次元配列で呼び出すか？)


'''

'''
これからの作業計画

modesのうちpositionを可変にする．     完了
positionの値を再入する変数を用意する．     完了
変数は[int,int]で入力させるようにする．    完了
load_gridのstart_pointに上記の組み合わせを送るようにする
'''


'''
二段階以上離れているマップをロードする場合の情報をどうやって保存するのか模索する必要あり．

'''




import pygame
import sys
from pygame.locals import*
import json
import csv
import mypackage.basic_setting as bs
import mypackage.load_function_v2 as load
import mypackage.save_function_v2 as save

SCREEN_SIZE = [500,500]




#カラーコード
color_code=bs.color_code

reverse_color_code ={v:k for (k,v) in color_code.items()}





#保存とロード
#get_atではrgb+不透明度の形式で取得


#階層構造の保存機能



#ver2の場合のマップ情報の抽出関数
#想定返り値はname，wide，length





#loadの関数









def main():

    #初期化
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("pymap ver2.2")
    screen.fill((255,255,255))
    current_color = (255, 0, 0,255)
    CELL_SIZE = 20
    input_text = ""
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    #色

    WHITE = (255, 255, 255,255)
    RED   = (255, 0, 0,255)
    GREEN = (0, 255, 0,255)
    BLUE  = (0, 0, 255,255)

    NONE = (0,0,0,0)

    #現在地
    
    current_coordinates=[0,0]

    #モード
    modes =bs.modes



    #マップの設定
    map_dot_num = [1000,1000]
    #max_CELL_num = [SCREEN_SIZE[0]//CELL_SIZE*2,SCREEN_SIZE[1]//CELL_SIZE*2]
    max_CELL_num = [map_dot_num[0]//CELL_SIZE*2,map_dot_num[1]//CELL_SIZE*2]
    display_map = [['w' for a in range(max_CELL_num[0])]for b in range(max_CELL_num[1])]

    sub_map = [['N' for a in range(max_CELL_num[0])]for b in range(max_CELL_num[1])]
    
    #直近のクリック位置保存(単位はドット)
    recent_click_cell = [0,0]


    #現在map表示しているのか階層表示しているのかを表す変数
    state_map = "map"
    state_hierarchy = "hierarchy"
    current_state = state_hierarchy

    #階層構造の初期設定
    hierarchy_buttons = []
    num_hierarchy = 1
    button_width = 200
    button_height = 60
    padding = 20

    #csvから階層構造データの読み取り
    is_exist_hierarchy,num_hierarchy,map_name_datas =load.load_hierarchy("hierarchy_v2/hierarchy_sample_v2.2.csv")

    #mapに記述する階層構造の情報の初期化
    stock_hierarchy = "None"

    #マップロードの開始場所
    load_start_point =[0,0]



    while True:
        clock.tick(30)

        print(f"\rsavemode= {modes['input_save']}, loadmode={modes['input_load']}, option={load_start_point[0]}-{load_start_point[1]} ,  "
               f"hierarchy=:{stock_hierarchy}, save_limited={modes['limited_save']} input:{input_text}                 ",end = '',flush = True)
        
        #階層構造表示用の仕組み仮置き場
        for i in range(num_hierarchy):
            hierarchy_button_x = 100
            hierarchy_button_y = 100 + i * (button_height + padding)
            rect = pygame.Rect(hierarchy_button_x, hierarchy_button_y, button_width, button_height)
            hierarchy_buttons.append({"rect": rect, "stage_id": i , "map_loc": f"mapdata_v2/mapdata_{map_name_datas[i]}.csv"})
        
        
        if (current_state == state_map):
            for k in range(max_CELL_num[1]):
                for i in range(max_CELL_num[0]):
                    cell_col = display_map[k][i]
                    color=color_code.get(cell_col,(255,255,255,255))
                    #描画位置拡張試し書き
                    pygame.draw.rect(screen, color, (((i-current_coordinates[0])*CELL_SIZE), ((k-current_coordinates[1])*CELL_SIZE), CELL_SIZE, CELL_SIZE))
                    #pygame.draw.rect(screen, color_code, ((i*CELL_SIZE), k*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        

        if (current_state == state_hierarchy):
            for button in hierarchy_buttons:
                pygame.draw.rect(screen, BLUE, button["rect"])
                text = font.render(f"hierarchy {button['stage_id']}F", True, WHITE)
                screen.blit(text, (button["rect"].x + 20, button["rect"].y + 15))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if current_state==state_map:
                    grid_x = (x // CELL_SIZE)+current_coordinates[0]
                    grid_y = (y // CELL_SIZE)+current_coordinates[1]
                    recent_click_cell = [grid_x,grid_y]
                    display_map[grid_y][grid_x]=reverse_color_code.get(current_color,'w')
                    
                    #pygame.draw.rect(screen, current_color, (grid_x*CELL_SIZE, grid_y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                if current_state==state_hierarchy:
                    for button in hierarchy_buttons:
                        if button["rect"].collidepoint(event.pos):
                            load.load_grid(button["map_loc"],display_map,[0,0],max_CELL_num)
                            current_state = state_map


            # キーで色変更
            elif event.type == pygame.KEYDOWN:
                if ((modes["input_save"]) | (modes["input_load"]) |(modes["hierarchy"]) | (modes["position"])) & (event.key != pygame.K_RETURN):#ENTERキーはエラーを発生させるため入力から除外すること
                    if event.key== pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                if event.key == pygame.K_r:
                    current_color = RED
                elif event.key == pygame.K_g:
                    current_color = GREEN
                elif event.key == pygame.K_b:
                    current_color = BLUE
                elif event.key == pygame.K_w:
                    current_color = WHITE
                elif (event.key == pygame.K_1):
                    if (modes["input_save"]==False):
                        bs.all_mode_off(modes)
                    modes["input_save"]= not(modes["input_save"])
                    input_text = ""
                elif (event.key == pygame.K_2):
                    if(modes["input_load"]==False):
                        bs.all_mode_off(modes)
                    modes["input_load"]= not(modes["input_load"])
                    input_text = ""
                elif (event.key == pygame.K_3):
                    if(modes["position"]==False):
                        bs.all_mode_off(modes)
                    modes["position"] = not(modes["position"])
                    input_text= ""
                elif (event.key == pygame.K_4):
                    if(modes["hierarchy"]==False):
                        bs.all_mode_off(modes)
                    modes["hierarchy"] = not(modes["hierarchy"])
                    input_text = ""
                elif (event.key == pygame.K_5) & (stock_hierarchy!="None"):
                    screen.fill((255,255,255))
                    is_exist_hierarchy,num_hierarchy,map_name_datas=load.status_hierarchy(stock_hierarchy)
                    if(is_exist_hierarchy):
                        current_state=state_hierarchy
                    else:
                        stock_hierarchy="None"
                elif(event.key== pygame.K_6):
                    modes["limited_save"] = not(modes["limited_save"])
                elif(event.key== pygame.K_7):
                    bs.all_mode_off(modes)
                    screen.fill((255,255,255))
                    current_state=state_hierarchy
                elif (event.key == pygame.K_RETURN) & (modes["input_save"] == True):
                    modes["input_save"] = False
                    if modes["limited_save"]:
                        save.save_grid(f"mapdata_v2/mapdata_v2_{input_text}.csv",CELL_SIZE,screen,input_text,500,500,display_map,stock_hierarchy,f"v2_{input_text}")
                    else:
                        save.save_grid(f"mapdata_v2/map_date_v2_{input_text}.csv",CELL_SIZE,screen,input_text,1000,1000,display_map,stock_hierarchy,f"v2_{input_text}")
                    stock_hierarchy = "None"
                elif (event.key == pygame.K_RETURN) & (modes["input_load"] == True):
                    modes["input_load"] = False
                    
                    load.load_grid(f"mapdata_v2/mapdata_v2_{input_text}.csv",display_map,load_start_point,max_CELL_num)
                elif (event.key == pygame.K_RETURN) & (modes["hierarchy"] == True):
                    modes["hierarchy"] = False
                    if(input_text!=""):
                        stock_hierarchy = input_text
                    else:
                        stock_hierarchy = "None"
                elif(event.key == pygame.K_RETURN) & (modes["position"]== True):
                    modes["position"]=False
                    if (input_text.count(",")==1):
                        try:
                            load_start_point = [int(start_point) for start_point in input_text.split(',')]
                        except:
                            print("エラー発生")

                elif (event.key == pygame.K_LEFT) & (current_coordinates[0]>0):
                    current_coordinates[0] -= 1
                elif (event.key == pygame.K_RIGHT) & (current_coordinates[0]<(max_CELL_num[0]-(SCREEN_SIZE[0]//CELL_SIZE))):
                    current_coordinates[0] += 1
                elif (event.key == pygame.K_UP) & (current_coordinates[1]>0):
                    current_coordinates[1] -= 1
                elif (event.key == pygame.K_DOWN) & (current_coordinates[1]<(max_CELL_num[1]-(SCREEN_SIZE[1]//CELL_SIZE))):
                    current_coordinates[1] += 1

        pygame.display.flip()
            

if __name__== "__main__":
    main()