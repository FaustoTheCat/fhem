import urllib
import urllib2
from flask import Flask
from flask import request

app = Flask(__name__)

def post_fhem(key, value):
        url = "http://127.0.0.1:8088/fhem?cmd=setreading%20Leaf%20" + key + "%20" + value + "&XHR=1"
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        page = response.read()
        return page

@app.route('/app', methods = ['GET', 'POST'])
def api_echo():
    if 'SOC' in request.args:
        post_fhem('BatterySOC', request.args['SOC'])
    if 'Ahr' in request.args:
        post_fhem('BatteryCapacity', request.args['Ahr'])
    if 'BatTemp' in request.args:
        post_fhem('BatteryTemp', request.args['BatTemp'])
    if 'Gids' in request.args:
        post_fhem('BatteryGids', request.args['Gids'])
    if 'Amb' in request.args:
        post_fhem('AmbientTemp', request.args['Amb'])
    if 'Long' in request.args:
        post_fhem('Long', request.args['Long'])
    if 'Lat' in request.args:
        post_fhem('Lat', request.args['Lat'])
    if 'Elv' in request.args:
        post_fhem('Elv', request.args['Elv'])
    if 'Trip' in request.args:
        post_fhem('Trip', request.args['Trip'])
    if 'Odo' in request.args:
        post_fhem('Odo', request.args['Odo'])
    if 'Seq' in request.args:
        post_fhem('Seq', request.args['Seq'])
    if 'PlugState' in request.args:
        post_fhem('PlugState', request.args['PlugState'])
    if 'ChrMode' in request.args:
        post_fhem('ChrMode', request.args['ChrMode'])
    if 'ChrPwr' in request.args:
        post_fhem('ChrPwr', request.args['ChrPwr'])
    if 'DevBat' in request.args:
        post_fhem('SmartphoneSOC', request.args['DevBat'])
    return ""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
