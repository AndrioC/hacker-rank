#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
	type_time = s[-2:]
	hour = int(s[0:2])
	minute = s[3:5]
	second =  s[6:8]
	new_hour = ''

	if type_time == 'PM' and hour != 12:
		new_hour = str(hour + 12)
	elif type_time == 'PM' and hour == 12:
		new_hour = str(hour)
	elif type_time == 'AM' and hour == 12:
		new_hour = '00'
	elif type_time == 'AM' and hour != 12:
		new_hour = '0'+str(hour)


	new_format = '{}:{}:{}'.format(new_hour,minute,second)

	return new_format

s = input()

result = timeConversion(s)

print(result)
