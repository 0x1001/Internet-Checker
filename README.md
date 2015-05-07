# Linux Server Tools

## Internet Check
Python script for checking internet connection for Linux.
Creates one log file per day and checks connection each 1 minute.
To start it in background use sh script that is part of this repository

## Raspberry Install Script
Basic installation script for Raspberry PI. Use it once you install Raspberry PI on SD card.

### Bash script
```sh
$ sudo ./install.sh
```


## Wifi auto reconnect
Automatically reconnects to Wifi network.

### Installation
 - Copy wifi/wifi_reconnect.sh to /etc/
 - Change group and owner to root
 - Change permission to 700
 - Add to crontab: * * * * * root /etc/wifi_reconnect.sh >> /var/log/syslog 2>&1
