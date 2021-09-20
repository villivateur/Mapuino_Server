from flask import Flask
from flask import request
from flask import jsonify

MapuinoApp = Flask(__name__)

database = {
    "ffffffff-ffff-ffff-ffff-ffffffffffff": {
        "DATA0": 0xffffffff,
        "DATA1": 0xffffffff,
    }
}

@MapuinoApp.route("/frontendAPI", methods=['POST'])
def putdate():
    if request.method == 'POST':
        new_data = {
            'DATA0': 0xffffffff,
            'DATA1': 0xffffffff,
        }
        database[request.form['UUID']] = new_data
        return "OK"

@MapuinoApp.route("/hardwareAPI", methods=['GET'])
def getdata():
    if request.method == 'GET':
        try:
            print(request.args.get('UUID'))
            resp = database[request.args.get('UUID')]
            resp['CODE'] = 0
        except Exception as e:
            print(e)
            resp = {'CODE': 1}
        return jsonify(resp)

if __name__ == "__main__":
    MapuinoApp.run("0.0.0.0", 7767)
