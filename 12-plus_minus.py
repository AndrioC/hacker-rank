#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

	sumPositive = 0
	sumNegative = 0
	sumZeros = 0
	size = len(arr)

	for x in arr:
		if x < 0:
			sumNegative += 1
		elif x == 0:
			sumZeros += 1
		else:
			sumPositive += 1	

	print('{:.6f}'.format(sumPositive/size))
	print('{:.6f}'.format(sumNegative/size))
	print('{:.6f}'.format(sumZeros/size))


n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
