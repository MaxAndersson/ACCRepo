#!/bin/bash
export C_FORCE_ROOT="true"
sudo service docker start
docker pull cellprofiler/cellprofiler:master
celery -A cposp_tasks worker -b $MASTER_IP --workdir=/home/ubuntu/ACCRepo
