
#!flask/bin/python
from flask import Flask, jsonify, render_template,request
#from urllib.parse import urlparse
import subprocess
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


app = Flask(__name__)


# Need to Source on master

def smog_conn():
    config = {'user':os.environ['OS_USERNAME'], 
              'key':os.environ['OS_PASSWORD'],
              'tenant_name':os.environ['OS_TENANT_NAME'],
              'authurl':os.environ['OS_AUTH_URL']}

    conn = swiftclient.client.Connection(auth_version=2, **config)
    nc = Client('2',**config)


def list_containers():
    # List containers
    (response, bucket_list) = conn.get_account()
    #for bucket in bucket_list:
    #    print bucket['name']

# UPLOAD PATH or listed files to container
'''
def upload_path():              

    import glob

    path = os.getcwd()
    print path

    #os.chdir('/Users/systemx/Desktop/cloud/projekt/cellprofilerfiles')


    cellprofilerpics = glob.glob('*.BMP')
    print cellprofilerpics

    for files in cellprofilerpics:
        test = file(files)
        testfile = test.read()
        conn.put_object("CPOSP-input", files, testfile)

    
    print "success"
'''



@app.route('/', methods = ['GET'])
def index():
    ## Sourced Env



    ##Not Sourced
    name = 'CPOSP'

    config = {'user':os.environ['OS_USERNAME'], 
              'key':os.environ['OS_PASSWORD'],
              'tenant_name':os.environ['OS_TENANT_NAME'],
              'authurl':os.environ['OS_AUTH_URL']}

    conn = swiftclient.client.Connection(auth_version=2, **config)
    nc = Client('2',**config)
    
    #smog_conn()
    #Just for testing DELETE
    #containers = {'name0': u'Cell13','name1': u'Cellprof','name2': u'tweets', 'name3': u'CPOSP-input', 'name4': u'ACCA', 'name5': u'CPOSP-output'}

    #Add when deploying
    
    #Container dict
    # List containers
    containers = {}
    (response, bucket_list) = conn.get_account()
    #print bucket_list
    xkey = 0
    for bucket in bucket_list:
        key = 'name'+str(xkey)
        containers[key] = bucket['name']
        xkey +=1
    
    return render_template('index.html', name=name, containers = containers) # containers = containers)

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
