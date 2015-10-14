from celery import Celery
import os
import sys


#Celery app object
celeryapp = Celery('tasks', backend='amqp', broker='amqp://')


#Running celery worker server:
# celery -A tasks.celeryapp worker --loglevel=info

@celeryapp.task(bind = True, name = "cellprofiler")   						
def cellprofiler_work(self):
	x=1


	return x


# Hämta data  (från public object storage)
# Separera datan..?
# Köra cellprofiler
# Forsla ut data igen!   VIlket format... csv eller mysql?
# Till databas eller concata csv filer
# Till public object storage?