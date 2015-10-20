#!/bin/bash

sudo rabbitmq-server start &
celery -A cposp_tasks worker --loglevel=info &

python -i runpy.py 
