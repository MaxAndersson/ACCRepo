
#!flask/bin/python
from flask import Flask, jsonify, render_template,request
#from urllib.parse import urlparse
#import subprocess
import sys
import os
import json
import swiftclient.client
import novaclient.client
import keystoneclient
import six
import time
from keystoneclient.auth.identity import v2 as identity
from keystoneclient import session
from novaclient.client import Client
from cposp_tasks import map_data


app = Flask(__name__)
config = {'user':os.environ['OS_USERNAME'],
              'key':os.environ['OS_PASSWORD'],
              'tenant_name':os.environ['OS_TENANT_NAME'],
              'authurl':os.environ['OS_AUTH_URL'],
               'auth_version': 2}
# hej !


conn = swiftclient.client.Connection(**config)

@app.route('/objects/')
def objects():
    container = request.values.getlist('container').pop()
    (response, ObjList) = conn.get_container(container)

    return json.dumps([obj['name'] for obj in ObjList])


def upload_path():

    import glob

    #path = os.getcwd()
    #print path

    #os.chdir('/Users/systemx/Desktop/cloud/projekt/cellprofilerfiles')   #Directory set by user!?


    cellprofilerpics = glob.glob('*.BMP')
    print cellprofilerpics

    for files in cellprofilerpics:
        test = file(files)
        testfile = test.read()
        conn.put_object("CPOSP-input", files, testfile)

    print "success"




@app.route('/', methods = ['GET'])
def index():
    print conn.get_auth()
    (response, bucket_list) = conn.get_account()
    return render_template('index.html', containers = [container['name'] for container in bucket_list]) # containers = containers)

@app.route('/run', methods = ['POST'])
def run():
    #config,input_name='CPOSP-input',output_name ='CPOSP-output', chunk_size = 10, meta_data = None
    print(config,
    request.form['input-container'],
    request.args.get('output-container'),
    request.args.get('chunk-size'),
    request.args.getlist('meta-data'),
    request.args.get('slave-count')
    )
    map_data(config,
    request.args.get('input-container'),
    request.args.get('output-container'),
    request.args.get('chunk-size'),
    request.args.getlist('meta-data'),
    request.args.get('slave-count')
    )
    return redirect('http://130.238.29.171:5000/')

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
