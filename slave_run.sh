#!/bin/bash
C_FORCE_ROOT=1
sudo service docker start
docker pull cellprofiler/cellprofiler:master
celery multi start -A cposp_tasks worker -b $MASTER_IP --workdir=/home/ubuntu/ACCRepo
