from celery import Celery
import os
import sys
import swiftclient.client


#Celery app object
celeryapp = Celery('tasks', backend='amqp', broker='amqp://CPOSP:CPOSP@CPOSP')


@celeryapp.task()
def aTask():
	return "Something"



def getandpartitionData():
    input_bucketURL = 'http://smog.uppmax.uu.se:8080/swift/v1/CPOSP-input/'
    output_bucketURL = 'http://smog.uppmax.uu.se:8080/swift/v1/CPOSP-output/'
    files = os.popen('curl {}'.format(input_bucketURL)).read().rsplit('\n')
    results = [cellprofiler_work(aFile, output_bucketURL) for aFile in files]


    return tasks.countMentionInTweetFile.delay(aFile,words)
