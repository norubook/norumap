import csv

#過去プログラム

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



#作成方針

'''
辞書形式を作成
該当コードが含まれていれば下の行をそのデータとして辞書に代入


(できれば)numpyを使用してマップデータの一括管理を行いたい
{map_data: a.csv,b.csv,c.csv}
を
map_data =[a.csv,b.csv,c.csv]に

'''



def load_hierarchy_v2_3(hierarchy_csv):
    output = {}
    try:
        with open(hierarchy_csv, "r",newline="",encoding="utf-8") as f:
            reader = csv.reader(f)
            code_row=next(reader)
            roop_count =0
            while(not("end_file_code9999" in code_row)):
                if "input_code0000" in code_row:
                    info_row=next(reader)
                    data_row = next(reader)
                    output[info_row[0]]=data_row
                code_row = next(reader)
                roop_count+=1
                if roop_count>50:
                    break                    

        return output
    except FileNotFoundError:
        return {}
