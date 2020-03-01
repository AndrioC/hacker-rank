#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):

	new_list = arr
	min_value = min(arr)
	list_cuts = []
	while min_value != 0:
		list_cuts.append(sum(i > 0 for i in new_list))
		for y in range(len(new_list)):
			if (new_list[y]):
				new_list[y] = new_list[y] - min_value
		min_value = min([i for i in new_list if i > 0], default=0)
		print(new_list)

	return list_cuts





n = int(input())

arr = list(map(int, input().rstrip().split()))

result = cutTheSticks(arr)

