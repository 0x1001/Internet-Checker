#!/bin/bash

IF=wlan0

wlan=`/sbin/ifconfig ${IF} | grep inet\ addr | wc -l`
if [ $wlan -eq 0 ]; then
    ifdown --force ${IF}
    ifup ${IF}
fi