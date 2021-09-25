from flask import Flask
from flask import request
from flask import jsonify
from amap_api import ip2province
from province2bitmap import province2bitmap

MapuinoApp = Flask(__name__)

database = {}

@MapuinoApp.route("/frontendAPI", methods=['GET'])
def putdate():
    if request.method == 'GET':
        print(request)
        if request.headers.getlist("X-Forwarded-For"):
            request_ip = request.headers.getlist("X-Forwarded-For")[0]
        else:
            return "NO_IP_ADDR"
        print(request_ip)
        province = ip2province(request_ip)
        if province == "error":
            return "IP_ADDR_ERROR"
        
        bitmap = province2bitmap(province[:2])
        print(bitmap)
        segment = bitmap[0]
        bit = bitmap[1]

        if not(request.args.get('UUID') in database):
            database[request.args.get('UUID')] = {
                "SEG0": 0x00000000,
                "SEG1": 0x00000000,
            }
        
        if segment == 0:
            database[request.args.get('UUID')]["SEG0"] |= (1 << bit)
        else:
            database[request.args.get('UUID')]["SEG1"] |= (1 << bit)

        return "OK"

@MapuinoApp.route("/hardwareAPI", methods=['GET'])
def getdata():
    if request.method == 'GET':
        try:
            resp = database[request.args.get('UUID')]
            resp['CODE'] = 0
            resp_json = jsonify(resp)
            database[request.args.get('UUID')]["SEG0"] = 0x00000000
            database[request.args.get('UUID')]["SEG1"] = 0x00000000
        except Exception as e:
            print(e)
            resp_json = jsonify({'CODE': 1})
        
        return resp_json

if __name__ == "__main__":
    MapuinoApp.run("0.0.0.0", 7767)
