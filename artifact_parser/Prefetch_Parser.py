import json, csv, os, re

def Prefetch(csv_files):
    csv_data = []
    data = {"ART0009" : {"name" : "Prefetch", "isEvent" : False, "data":[]}}
    exts = '''.exe|.pdf|.hwp|.doc|.docm|.docx|.dot|.dotx|.csv|.ppt|.pptm|.pptx|.xlm|.xls|.xlsm|.xlsx|.zip|.rar|.7z'''
    for csv_file in csv_files:
        try:
            with open(csv_file, 'rt', encoding="utf-8") as f:
                csvReader = csv.DictReader(f)

                for rows in csvReader:
                    csv_data.append(rows)
        except:
            pass

    for item in csv_data:
        itemd = item.copy()

        Ndel = ["ExecutableName", "FilesLoaded", "LastRun"]

        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]

        my_list = item["FilesLoaded"].split(',')
        files = []

        for file in my_list:
            if len(re.compile(exts, re.I).findall(os.path.basename(file))) != 0:
                files.append(os.path.basename(file))

        if files == []:
            continue
        
        item["FilesLoaded"] = files

        item["실행확장자"] = item.pop("ExecutableName")
        item["접근파일"] = item.pop("FilesLoaded")
        item["최근실행시간"] = item.pop("LastRun")

        data["ART0009"]["data"].append(item)

    with open(r"ART0009_Prefetch.json", "w", encoding='utf-8') as json_file: 
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        json_file.close()