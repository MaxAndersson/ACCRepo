
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

'''
config = {'user':os.environ['OS_USERNAME'], 
          'key':os.environ['OS_PASSWORD'],
          'tenant_name':os.environ['OS_TENANT_NAME'],
          'authurl':os.environ['OS_AUTH_URL']}

conn = swiftclient.client.Connection(auth_version=2, **config)
nc = Client('2',**config)
'''

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

    containers = {'name11': u'Cell13', 'name12': u'CellP-data', 'name13': u'CellP-output', 'name16': u'Cellprof', 'name17': u'FarezCon', 'name19': u'JustAnotherContainer', 'name78': u'testContainer_Saim', 'name79': u'testContainerrrr', 'name72': u'my_bucket_01', 'name73': u'noaabukk', 'name70': u'my-test-bucket', 'name71': u'my_bucket', 'name76': u'saim-bucket', 'name77': u'testContainer', 'name74': u'ruul_bucket_ah', 'name75': u'ryman', 'name86': u'tweets', 'name85': u'testcontainerr', 'name84': u'testcontainerS', 'name83': u'testcontainerKalle', 'name82': u'testcontainerAndrew', 'name81': u'testcontainer2', 'name80': u'test_bucket', 'name69': u'molns_storage_44913206-6722-417e-a20f-5d855938cab9', 'name68': u'lufr2071', 'name61': u'lab2ML_45686723-e3ab-46e4-97f7-7bfad4c8fe7b', 'name60': u'lab2ML_35344db4-c626-4e8c-917d-93c8682c6175', 'name63': u'lab2ML_c68f173d-36e7-4d47-bb2d-3337aeab1ee2', 'name62': u'lab2ML_6d0f0d8f-5255-49f5-a3ac-89bf6190a415', 'name65': u'lab2ML_e0439fec-19d0-4d60-984e-2bf6422c353e', 'name64': u'lab2ML_dd159c4a-5954-44c2-a797-04e7bd516c51', 'name67': u'lufr', 'name66': u'ljoni2138', 'name6': u'A_b989361a-b156-4eb7-b0c2-f747aa13ae31', 'name7': u'CPOSP-input', 'name4': u'AJ_bc9904ef-9f6d-4c87-b2d8-ed8bbe9ac8e4', 'name5': u'A_a8b211e2-d7e0-4016-bf30-2075ad07158e', 'name2': u'AJ_48c95173-4b77-467d-aa64-c934f3efeb5a', 'name3': u'AJ_5cda2de6-f80c-40db-9ab6-d189dd1946fb', 'name0': u'ACCA', 'name1': u'ACC_T16', 'name8': u'CPOSP-output}


'''
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
'''
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
