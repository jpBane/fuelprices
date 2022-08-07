# fuelprices
Logging fuelprices to a database and visualise the data in a grafana dashboard

## What you need
Parts list:
* a computer with Linux on it (I use a Raspberry Pi)
* ...

Software:
* Linux operating system
* InfluxDB
* Grafana

## Setting up the database
...install it: `sudo apt install influxdb`

...run it: type `influx` into the command prompt.

set up the database inside the influx console: `CREATE DATABASE <database_name>`

## Python script for data logging
...you need the following packages:
* requests
* influxdb

You can check if they are already installed by typing the folling command into your command prompt: `pip3 list | grep 'requests\|influxdb'` (you need to escape the "|" with a "\\" to ensure that it is recognised as a meta-character [Link](https://linuxize.com/post/grep-multiple-patterns/)). You can install missing packages by the following command:`pip3 install <package name>`. 

...use the `fuelprices.py` script... You have to set the following paramters... 
* the name of the dabase you created earlier
* ...

Due to the terms of use for the API we are not allowed to query more than once in five minutes. Therefore we set a cronjob by `crontab -e` and add  the following line `*/6 * * * * /path/to/python3 /path/to/fuelprices.py /dev/null 2>&1`. 

## Setting up the dashboard
...in case grafana is not installed already...


