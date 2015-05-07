#!/bin/bash

IP=8.8.8.8
IF=ra0

ping -c4 ${IP} > /dev/null

if [ $? != 0 ]
then
    logger -t $0 "Wifi reconnect"
    ifdown --force ${IF}
    ifup ${IF}
fi

