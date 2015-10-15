from celery import Celery
import os
import sys
import swiftclient.client


#Celery app object
celeryapp = Celery('tasks', backend='amqp', broker='amqp://')




def main():
	
	
return "Done"



def getandpartitionData():
    input_bucketURL = 'http://smog.uppmax.uu.se:8080/swift/v1/CPOSP-input/'
    output_bucketURL = 'http://smog.uppmax.uu.se:8080/swift/v1/CPOSP-output/'
    files = os.popen('curl {}'.format(input_bucketURL)).read().rsplit('\n')
    results = [cellprofiler_work(aFile, output_bucketURL) for aFile in files]


    return tasks.countMentionInTweetFile.delay(aFile,words)



#Running celery worker server:
# celery -A tasks.celeryapp worker --loglevel=info

@celeryapp.task(bind = True, name = "cellprofiler")   						
def cellprofiler_work(file, output):
	x=1
	return x



#load and source rc file? 
# Hämta data  (från public object storage)
# Separera datan..?
# Köra cellprofiler
# Forsla ut data igen!   Vilket format... csv eller mysql?
# Till databas eller concata csv filer
# Till public object storage?






if __name__ == '__main__':
    main()
