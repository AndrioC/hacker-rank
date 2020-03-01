#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def repeatedString(s, n):
	list_string = list(s)
	count_value_a = 0

	if len(list_string) == 1:
		if s == 'a':
			return n
		else:
			return 0
	
	count_value_a = list_string.count('a')
	num_times = math.floor(n/len(s))
	new_string = count_value_a * num_times
	new_string += list_string[:(n%len(s))].count('a')

	return new_string

s = input()

n = int(input())

result = repeatedString(s, n)
print(result)

