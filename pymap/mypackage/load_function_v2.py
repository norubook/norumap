import csv


def load_ver2(map_info_row,start_point):
    #仮置き返り値
    map_info =[]
    connect_info ={}

    for i in map_info_row[:2]:
        map_info.append(i)
    for k in map_info_row[3:]:
        split_connect_info = k.strip().split(":")
        if (len(split_connect_info)==3):
            key,values = split_connect_info[0].strip(),list(map(int,split_connect_info[1:]))
            if (key not in connect_info):
                values[0]+=start_point[0]
                values[1]+=start_point[1]
                connect_info[key] = values
    
    
    keys = list(connect_info.keys())
    #print(f"\n\n{connect_info[keys[0]]}")
    return map_info,connect_info  #,keys



def load_grid(filename,display_map,start_point,max_CELL_num):
    global grid
    try:
        with open(filename, "r",newline="") as f:
            reader = csv.reader(f)
            k=start_point[1]
            #サイズ変更後の処理を設定後下記を適用してサイズを取得してください
            map_info_row=next(reader)
            if(map_info_row[0]=="ver2"):
                map_info,connect_info =load_ver2(map_info_row,[0,0])
            
            for row in reader:
                for i in range(len(row)):
                    cell_col = row[i]
                    point_i=i+start_point[0]
                    if((point_i<max_CELL_num[0]) & (k<max_CELL_num[1])):
                        display_map[k][point_i]=cell_col
                    #描画位置拡張試し書き
                    #pygame.draw.rect(screen, color_code, ((i*CELL_SIZE)-current_coordinates, (k*CELL_SIZE)-current_coordinates, CELL_SIZE, CELL_SIZE))
                    #pygame.draw.rect(screen, color_code, ((i*CELL_SIZE), k*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                k+=1
        k=0
            
        

        j =0
        for key in connect_info:
            
            start_point = [connect_info[key][0],connect_info[key][1]]
            with open(f"pymap/pymap/mapdata_v2/mapdata_v2_{key}.csv" ,"r",newline="") as f:
                reader = csv.reader(f)
                k=start_point[1]
                #サイズ変更後の処理を設定後下記を適用してサイズを取得してください
                map_info_row=next(reader)
                if(map_info_row[0]=="ver2"):
                    map_info,connect_info_2 =load_ver2(map_info_row,start_point)

                for row in reader:
                    for i in range(len(row)):
                        cell_col = row[i]
                        point_i=i+start_point[0]
                        if((point_i<max_CELL_num[0]) & (k<max_CELL_num[1])):
                            display_map[k][point_i]=cell_col
                        #描画位置拡張試し書き
                        #pygame.draw.rect(screen, color_code, ((i*CELL_SIZE)-current_coordinates, (k*CELL_SIZE)-current_coordinates, CELL_SIZE, CELL_SIZE))
                        #pygame.draw.rect(screen, color_code, ((i*CELL_SIZE), k*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    k+=1



        print("\r読み込み完了。             \n",end = '',flush = True)
    except FileNotFoundError:
        print("\r保存ファイルが見つかりませんでした。               ",end = '',flush = True)


def load_hierarchy(hierarchy_csv):
    try:
        with open(hierarchy_csv, "r",newline="") as f:
            reader = csv.reader(f)
            #サイズ変更後の処理を設定後下記を適用してサイズを取得してください
            hierarchy_info_row=next(reader)
            map_info_row=next(reader)

        return 1,int(hierarchy_info_row[2]),map_info_row
    except FileNotFoundError:
        return 0,0,["None"]

def status_hierarchy(hierarchy_name):
    hierarchy_file_pass =f"pymap/pymap/hierarchy_v2/hierarchy_{hierarchy_name}.csv"
    is_exist_hierarchy,num_hierarchy,map_name_datas =load_hierarchy(hierarchy_file_pass)
    return is_exist_hierarchy,num_hierarchy,map_name_datas







"load部分に不具合？物によってロードされない"