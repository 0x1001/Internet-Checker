#!/bin/bash

# Disabling swap to extend SD card life
swapoff --all
apt-get remove dphys-swapfile

# Installation script for Raspberry PI
apt-get update

# MC
apt-get install -y mc

# VNC
apt-get install -y tightvncserver
apt-get install -y autocutsel
cp vncboot /etc/init.d/
chmod 755 /etc/init.d/vncboot
update-rc.d vncboot defaults
su - pi -c "tightvncserver"
cp -f xstartup /home/pi/.vnc
chmod +x /home/pi/.vnc/xstartup

# PIP
apt-get install -y python-pip

# Ninja
#apt-add-repository ppa:ninja-ide-developers/daily
apt-get update
apt-get install -y ninja-ide
if [ ! -d "/home/pi/Desktop" ]; then
mkdir /home/pi/Desktop
fi
cp ninja-ide.desktop /home/pi/Desktop/


# Proftpd
apt-get install -y proftpd

# Rdate
apt-get install -y rdate
rdate -s time.nist.gov
echo "0 * * * * root rdate -s time.nist.gov" >> /etc/crontab

# Pydev
apt-get install -y python-dev

# Screen
apt-get install -y screen
