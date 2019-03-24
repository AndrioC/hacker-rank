#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

	sum_total = 0
	operations_list = []

	for x in arr:
		sum_total += x

	for x in arr:
		operations_list.append(sum_total - x)

	print(min(operations_list), max(operations_list))


arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)
