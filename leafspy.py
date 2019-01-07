import urllib
import urllib2
import logging
from flask import Flask
from flask import request

import os
import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("/home/pi/logfile.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()
logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('access.log')
logger.addHandler(handler)

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
    if 'ChrgMode' in request.args:
        post_fhem('ChrgMode', request.args['ChrgMode'])
    if 'Wpr' in request.args:
        post_fhem('Wpr', request.args['Wpr'])  
    if 'VIN' in request.args:
        post_fhem('VIN', request.args['VIN'])
    if 'ChrgPwr' in request.args:
        post_fhem('ChrgPwr', request.args['ChrgPwr'])
    if 'DevBat' in request.args:
        post_fhem('SmartphoneSOC', request.args['DevBat'])
    return ""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
