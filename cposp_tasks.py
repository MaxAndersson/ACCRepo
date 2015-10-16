from celery import Celery
import os
import sys
import swiftclient.client


#Celery app object
celeryapp = Celery('tasks', backend='amqp', broker='amqp://CPOSP:CPOSP@CPOSP')

'''
testing
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('for_task_A', Exchange('for_task_A'), routing_key='for_task_A'),
    Queue('for_task_B', Exchange('for_task_B'), routing_key='for_task_B'),
)

CELERY_ROUTES = {
    'my_taskA': {'queue': 'for_task_A', 'routing_key': 'for_task_A'},
    'my_taskB': {'queue': 'for_task_B', 'routing_key': 'for_task_B'},
}
'''


#http://docs.celeryproject.org/en/latest/reference/celery.html#celery.group
# Creates a group of tasks to be executed in parallel.



@celeryapp.task()
def aTask():
	return "Something"



def getandpartitionData():
    input_bucketURL = 'http://smog.uppmax.uu.se:8080/swift/v1/CPOSP-input/'
    output_bucketURL = 'http://smog.uppmax.uu.se:8080/swift/v1/CPOSP-output/'
    files = os.popen('curl {}'.format(input_bucketURL)).read().rsplit('\n')
    results = [cellprofiler_work(aFile, output_bucketURL) for aFile in files]


    return tasks.countMentionInTweetFile.delay(aFile,words)
