#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):

	distances = []

	for x in range(len(a)):
		for y in range(len(a)-1):
			if (a[x] == a[y+1]) and (x != y+1):
				distances.append(abs(x-(y+1)))

	if len(distances) > 0:
		return min(distances)
	else:
		return -1



n = int(input())

a = list(map(int, input().rstrip().split()))

result = minimumDistances(a)

print(result)