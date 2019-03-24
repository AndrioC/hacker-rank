#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	#The logic is pretty simple. We take D as -1 value and U as +1 value, when the sum is equal zero so he is at the sea level, so he enters a leaves one valley
	list_path = list(s)

	sum_path = 0
	valley_number = 0

	for x in range(n):
		if s[x] == 'D':
			value = -1
			sum_path += value
		else:
			value = +1
			sum_path += value

			if sum_path == 0:
				valley_number += 1

	return valley_number
n = int(input())

s = input()

result = countingValleys(n, s)
print(result)
