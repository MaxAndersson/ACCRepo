from celery import Celery
import os
import sys


#Celery app object
celeryapp = Celery('tasks', backend='amqp', broker='amqp://')