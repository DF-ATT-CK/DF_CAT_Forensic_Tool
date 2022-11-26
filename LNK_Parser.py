import json, xmltodict

def Shortcut_LNK_Files(userprofile):
    data = {"ART0022":{"name":"Shortcut_LNK_Files", "isEvent":False, "data":[]}}
    
    with open(r"{}\Shortcut_LNK_Files.xml".format(userprofile), encoding='euc-kr') as xml_file: 
        data_dict = xmltodict.parse(xml_file.read())

    xml_file.close()
    
    for item in data_dict["shortcuts_list"]["item"]:
        del item['broken_shortcut']
        del item['link_to']
        del item['arguments']
        del item['start_in']
        del item['hot_key']
        del item['location']
        del item['comment']
        
        item["이름"] = item.pop("shortcut_name")
        item["수정시간"] = item.pop("modified_date")
        item["경로"] = item.pop("shortcut_filename")
        
        data["ART0022"]["data"].append(item)

    json_data = data

    with open("ART0022_Shortcut_LNK_Files.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()