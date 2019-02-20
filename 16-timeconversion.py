'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.


-Function Description-

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

s: a string representing time in 12 hour format

-Input Format-

A single string s containing a time in 12-hour clock format (i.e.hh:mm:ssAM or hh:mm:ss:PM), where 01 <= hh <= 12 and 00 <= mm,ss <= 59.

-Constraints-

-> All input times are valid

-Output Format-

Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

-Sample Input-

07:05:45PM

-Sample Output-

19:05:45


'''

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