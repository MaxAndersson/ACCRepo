#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y python-pip #rabbitmq-server  python-h5py python-zmq python-matplotlib cython openjdk-7-jdk python-wxgtk2.8 python-scipy python-mysqldb python-vigra --fix-missing
sudo pip install celery &
sudo pip install python-keystoneclient
sudo pip install python-swiftclient
wget -qO- https://get.docker.com/ | sh
sudo service docker start
docker pull cellprofiler/cellprofiler:master
celery -A cposp_tasks worker -b $MASTER_IP &
