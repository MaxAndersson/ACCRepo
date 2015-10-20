#!/bin/bash
if [ -z "$1" ]; then
    echo usage: $0 master,slave
    exit
elif [ "$1" = "master" ]; then
    chmod 777 ./master.sh
    ./master.sh
    exit

elif [ "$1" = "slave" ]; then
    chmod 777 ./slave.sh
    ./slave.sh -c
    exit

fi
