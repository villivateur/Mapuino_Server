import requests
import json

amap_api_key = "xxxxxxxxxxxxxxxxxxxxx"

def ip2province(ip_address):
    r = requests.get(f"https://restapi.amap.com/v3/ip?ip={ip_address}&output=json&key={amap_api_key}")
    if r.status_code != 200:
        return "error"
    data = json.loads(r.text)
    if data["status"] != "1":
        return "error"
    elif data["province"] == []:
        return "world"
    else:
        return data["province"]
