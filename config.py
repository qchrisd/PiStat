'''
Written by: Chris Quartararo
2019-07-31

Main configuration for the PiStat V2. Contains the commonly used directories and commonly used vars.

'''

# Import dependencies
import os
import csv

# Project directories
currentDir = os.path.abspath('.')  # Current directory
projectDir = os.path.expanduser('~/PiStatV2')

# 1 Wire device mount point
deviceDir = os.path.dirname('/sys/bus/w1/devices/')

# Builds a dictionary of devices
devices = dict()
with open('devices.csv', mode='r') as devFile:
	reader = csv.DictReader(devFile)
	for row in reader:
		devices[row['Name']] = {'serial':row['Serial'].strip(), 'offset':row['Offset'], 'zone': row['Zone']}

# Lists the names of the devices
deviceNames = [dev for dev in devices]


