
#!flask/bin/python
from flask import Flask, jsonify, render_template,request
#from urllib.parse import urlparse
import subprocess
import sys
import os
import json

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    ## Sourced Env


    ##Not Sourced


    name = 'Max'
    return render_template('index.html', name=name)
@app.route('/checkAddress')
def checkAddress():
    try:
        url = os.popen('curl {}'.format(request.values.getlist('url').pop())).read()
        url = json.loads(url)
        if url['version']['status'] == "stable" and url['version']['id'] == 'v2.0':
            return json.dumps({'status':'ok'})
        else:
            return json.dumps({'status':'failed'})
    except Exception:
        return json.dumps({'status':'failed'})

@app.route('/identity',methods = ['GET','POST'])
def osIdentity():

    return str(request.values.getlist('identity'))



if __name__ == '__main__':

    app.run(host='0.0.0.0',debug=True)
