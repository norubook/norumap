
import csv

def save_hierarchy(hierarchy_name,map_name):
    hierarchy_file_pass =f"pymap/pymap/hierarchy_v2/hierarchy_{hierarchy_name}.csv"
    new_rows =[]
    with open(hierarchy_file_pass, newline='') as f:
        reader = csv.reader(f)
        row = next(reader)
        if(len(row)>=3):
            row[2] = str(int(row[2])+1)
            new_rows.append(row)
        row= next(reader)
        row.append(map_name)
        new_rows.append(row)

    #記入
    with open(hierarchy_file_pass, "w",newline="") as f:
        writer =csv.writer(f)
        writer.writerows(new_rows)


    

'''

filenameとmapnameは後で上手に変換したい


'''
def save_grid(filename,CELL_SIZE,screen,name_data,wide,length,display_map,hierarchy_name,map_name):
    with open(filename, "w",newline="") as f: #newlineを外すと改行がおかしくなるため注意
        list =[]
        writer = csv.writer(f)
        #1行目データ
        list.extend(["ver2",name_data,wide,length])
        writer.writerow(list)
        list=[]
        for i in range(length//CELL_SIZE):
            list=(display_map[i])
            writer.writerow(list)
        if(hierarchy_name!="None"):
            save_hierarchy(hierarchy_name,map_name)
    print("保存しました。")