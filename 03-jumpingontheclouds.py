#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def jumpingOnClouds(c):
	list_path = list(c)

	sum_path = 0
	x = 0

	while x < len(list_path) - 1:
		if (x+2 <= len(list_path)-1 and (list_path[x+2] == 0)):
			x += 2
			sum_path += 1
		elif (list_path[x+1] == 0):
			x += 1
			sum_path +=1
	return sum_path

n = int(input())

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c)
print(result)

#50
#0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0

#28


#100
#0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 0 1 0 0 0 0 0 0 1 0 0 0

#53
