from celery import Celery
import os
import sys
import swiftclient.client
import keystoneclient
from itertools import islice
import urllib2
#Celery app object
celery = Celery('tasks', backend='amqp', broker='amqp://')
# broker='amqp://CPOSP:CPOSP@CPOSP')

#http://docs.celeryproject.org/en/latest/reference/celery.html#celery.group
# Creates a group of tasks to be executed in parallel.



@celery.task()
def aTask():
	return "Something"


def downloadFile(url,path):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(path + file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,
    f.close()
    return file_name

def make_path(name,request_id):
        namespace = name + '-' + request_id
        if os.path.exists(namespace):
                return namespace
        else:
                os.makedirs(namespace)
                return namespace 
def has_pipeline(url,input_path, name):
        local_path = input_path + '/' + name 
        if os.path.exists(local_path):
                return local_path
        else:
                remote_path = url + name
                downloadFile(remote_path, input_path)
                return local_path

@celery.task(bind=True)
def cposp_work(self,input_url,chunks,output_config,output_name):
    request_id = self.request.id
    urls= [input_url + chunk for chunk in chunks]
    conn = swiftclient.client.Connection( **output_config)
    input_path =  make_path('input',request_id)
    output_path = make_path('output',request_id)
    pipline_path = has_pipeline(input_url,input_path, 'CP_translocation_pipeline.cppipe') ## Get pipeline from master instead.
    filelist_path = input_path + '/' + 'filelist.txt' 
    print input_path,output_path,pipeline_path,filelist_path
    f = open(filelist_path,'wr')
    for url in urls:
        f.write(url + '\n')
    f.close()
    os.popen('sudo docker run -v {}:/input -v {}:/output  cellprofiler/cellprofiler:master -i /input -o /output -p {} --file-list=/input/{}'.format(input_path,output_path,pipline_path,filelist_path))
    outputs = os.listdir(output_path)
    for output_file in outputs:
        conn.put_object(output_name,output_path +'/' + output_file,open(output_path + '/' + output_file ))

def map_data(input_url= None,output_url = None, chunk_size = 10):
    client_config = os.environ
    config = {
                'user' : client_config['OS_USERNAME'],
                'key' : client_config['OS_PASSWORD'],
                'tenant_name' : client_config['OS_TENANT_NAME'],
                'authurl' : client_config['OS_AUTH_URL'],
                'auth_version': 2,
    }
    #
#    return [obj['name'] for obj in conn.get_account()[1]]

    input_bucketURL = 'http://smog.uppmax.uu.se:8080/swift/v1/CPOSP-input/'
    output_name = 'CPOSP-output'
    #output_bucketURL = 'http://smog.uppmax.uu.se:8080/swift/v1/CPOSP-output/'
    files = os.popen('curl {}'.format(input_bucketURL)).read().rsplit('\n')
    #Apply image filter.

    file_length = len(files)
    chunks_count = file_length/chunk_size
    rest = file_length%chunk_size
    
    for index in range(0,chunks_count):
    
        start = chunk_size * index
        stop = chunk_size * (index+1)
        if index == chunks_count-1 and rest != 0:
            stop = stop + rest-1 ## VERRY VERRY BADDD BOY !
        cposp_work.delay(input_bucketURL,files[start:stop],config,output_name)
    

#    results = [cellprofiler_work(aFile, output_bucketURL) for aFile in files]


 #   return tasks.countMentionInTweetFile.delay(aFile,words)


