'''
Written by: Chris Quartararo
2019-07-31

Main configuration for the PiStat V2. Contains the commonly used directories and variables.

'''

# Import dependencies
import os
import csv
import copy

# Project directories
currentDir = os.path.abspath('.')  # Current directory
projectDir = os.path.expanduser('~/PiStatV2')

# 1 Wire device mount point
deviceDir = os.path.dirname('/sys/bus/w1/devices/')


# Builds a dictionary of devices from the devices.csv file
devices = dict()
with open('devices.csv', mode='r') as devFile:
	reader = csv.DictReader(devFile)
	for row in reader:
		devices[row['Name']] = {'serial':row['Serial'].strip(), 'offset':row['Offset'], 'zone': row['Zone']}

# Builds a list of w1 serial numbers connected to the device
connectedDeviceSerials = [serial for serial in os.listdir(deviceDir)]

# Lists the names of the devices
deviceNames = [dev for dev in devices]

# Builds a dictionary of devices from devices.csv that are connected
devicesConnected = dict()
for dev in devices:
	if devices[dev]['serial'] in connectedDeviceSerials:
		devicesConnected[dev] = devices[dev]
	else:
		pass

# Builds a dictionary of devices from devices.csv that are not connected
devicesDisconnected = dict()
for dev in devices:
	if devices[dev]['serial'] not in connectedDeviceSerials:
		devicesDisconnected[dev] = devices[dev]
	else:
		pass

# Builds a dictionary of devices not in devices.csv that are connected
devicesNew = copy.deepcopy(connectedDeviceSerials)
for dev in devices:
	if devices[dev]['serial'] in devicesNew:
		devicesNew.remove(devices[dev]['serial'])
	else:
		pass


# Displays all devices passed to method with Serial #, Zone, and Offset in degrees C
def displayDevices(devs):
	for dev in devs:
		try:
			print(dev + ' (' + devs[dev]['serial'] + '): Zone '
				+ devs[dev]['zone'] + ', Offset ' + devs[dev]['offset']
				+ '\N{DEGREE CELSIUS}')
		except:
			print('No devices found or bad dict')

