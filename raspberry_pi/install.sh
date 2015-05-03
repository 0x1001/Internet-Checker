#!/bin/bash

# Installation script for Raspberry PI

apt-get update

# MC
apt-get install -y mc

# VNC
apt-get install -y tightvnc
cp vncboot /etc/init.d/
chmod 755 /etc/init.d/vncboot
tightvncserver

# PIP
apt-get install python-pip

# Ninja
apt-add-repository ppa:ninja-ide-developers/daily
apt-get update
apt-get install -y ninja-ide
cp ninja-ide.desktop /home/pi/Desktop/

