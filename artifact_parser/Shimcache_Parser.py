import json, csv, os

def Shimcache(userprofile):
    data = {"ART0010" : {"name" : "ShimCache", "isEvent" : False, "data":[]}}
    csv_data = []
    with open("{}\\Shimcache.csv".format(userprofile), 'rt', encoding="utf-8") as f:
        csvReader = csv.DictReader(f)
        
        for rows in csvReader:
            csv_data.append(rows)

    for item in csv_data:
        itemd = item.copy()

        Ndel = ["Path", "LastModifiedTimeUTC"]

        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]

        data["ART0010"]["data"].append({"이름" : os.path.basename(item["Path"]), "경로" : item["Path"], "수정시간" : item["LastModifiedTimeUTC"]})

    with open(r"ART0010_ShimCache.json", "w", encoding='utf-8') as json_file: 
        json.dump(data, json_file, indent=4, ensure_ascii=False)
        json_file.close()