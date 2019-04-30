#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

	sum_leap_year = 244
	sum_not_leap_year = 243

	if (year == 1918):
		new_format = "{}.{}.{}".format('26','09',year)
	elif ((year <= 1917 and year % 4 == 0) or ((year > 1918 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))):
		new_format = "{}.{}.{}".format(256-sum_leap_year,'09',year)
	else:
		new_format = "{}.{}.{}".format(256-sum_not_leap_year,'09',year)

	return new_format





year = int(input().strip())

result = dayOfProgrammer(year)
print(result)

