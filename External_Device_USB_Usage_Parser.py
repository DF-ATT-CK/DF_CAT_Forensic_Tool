import json, xmltodict

def External_Device_USB_Usage(userprofile):
    data = {"E0006" : {"name" : "External_Device_USB_Usage", "isEvent" : True, "data":[]}}
    
    with open("{}\\External_Device_USB_Usage.xml".format(userprofile), encoding='euc-kr') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

    xml_file.close()
    
    for item in data_dict["usb_devices_list"]["item"]:
        itemd = item.copy()
        
        Ndel = ["description", "device_type", "serial_number", "registry_time_1", "registry_time_2", "driver_description", "instance_id", "capabilities"]
        
        for key in itemd.keys():
            num = 0
            for n in Ndel:
                if key != n:
                    num += 1
                if num == len(Ndel):
                    del item[key]
        
        item["장치 설명"] = item.pop("description")
        item["장치 종류"] = item.pop("device_type")
        item["장치 등록번호"] = item.pop("serial_number")
        item["생성날짜"] = item.pop("registry_time_1")
        item["최근 연결날짜"] = item.pop("registry_time_2")
        item["드라이버 설명"] = item.pop("driver_description")
        item["인스턴스 ID"] = item.pop("instance_id")
        item["능력 및 용량"] = item.pop("capabilities")
        
        data["E0006"]["data"].append(item)

    json_data = data

    with open("E0006_External_Device_USB_Usage.json", "w", encoding='utf-8') as json_file: 
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        json_file.close()