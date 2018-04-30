'''Extract datetimes from log entries and calculate the time
	 between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
# logfile = os.path.join('/tmp', 'log')
# urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)


logfile = 'messages.log.txt'
# for you to code:

def convert_to_datetime(line):

	year = re.findall(r'\d{4}',line)
	other_values = re.findall(r'\d{2}',line)
	other_values = other_values[2:7]
	year = int(year[0])
	month = int(other_values[0])
	day = int(other_values[1])
	hour = int(other_values[2])
	minute = int(other_values[3])
	second = int(other_values[4])

	# print(type(int(year[0])))
	date_time= datetime(year, month, day, hour, minute, second)
	return date_time
	# print(year)
	'''TODO 1:
		 Given a log line extract its timestamp and convert it to a datetime object.
		 For example calling the function with:
		 INFO 2014-07-03T23:27:51 supybot Shutdown complete.
		 returns:
		 datetime(2014, 7, 3, 23, 27, 51)'''


def time_between_shutdowns(loglines):
	shutdown_lines = []
	for line in loglines:
		if SHUTDOWN_EVENT in line:
			shutdown_lines.append(line)
	return shutdown_lines

		# '''TODO 2:
		# 	 Extract shutdown events ("Shutdown initiated") from loglines and calculate the
		# 	 timedelta between the first and last one.
		# 	 Return this datetime.timedelta object.'''

# def select_line(file, line_number):


with open(logfile) as f:
	loglines = f.readlines()
	shutdown_lines =  time_between_shutdowns(loglines)
	shutdown_times = []
	for line in shutdown_lines:
		time = convert_to_datetime(line)

		shutdown_times.append(time)
		# print(str(time))
	# print(str(time_delta))
	time_delta = []
	for i in range(len(shutdown_times)-1):
		delta = (shutdown_times[i+1] - shutdown_times[i])
		time_delta.append(delta)


	print(str(time_delta[0]))





	# select_line(loglines, 3)
		# for line in loglines:
		# 	line_split = line.split(' ')
		# 	time_stamp = line_split[1]
		# 	convert_to_datetime(time_stamp)

