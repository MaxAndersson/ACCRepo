# #!/bin/bash
# if [ -z "$1" ]; then
#     echo usage: $0 -c Contextualize
#     exit
# elif [ "$1" = "-c" ]; then
  sudo apt-get update -y
  sudo apt-get install -y python-pip #rabbitmq-server  python-h5py python-zmq python-matplotlib cython openjdk-7-jdk python-wxgtk2.8 python-scipy python-mysqldb python-vigra --fix-missing
  sudo pip install celery &
  sudo pip install python-keystoneclient
  sudo pip install python-swiftclient
  wget -qO- https://get.docker.com/ | sh
  sudo service docker start
  docker pull cellprofiler/cellprofiler:master
  mkdir input
  mkdir -m 777 output
#
# elif [ "$1" = "-w" ]; then
#   #sudo apt-get update -y
#   sudo service docker start
#   celery -A cposp_tasks worker &
#
# elif [ "$1" = "-r" ]; then


  # export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
  # export LD_LIBRARY_PATH=/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server:/usr/lib/jvm/java-7-openjdk-amd64:/usr/lib/jvm/java-7-openjdk-amd64/include
  # git clone https://github.com/CellProfiler/CellProfiler
  # cd CellProfiler/ || exit
  # git checkout 2.1.1




fi
