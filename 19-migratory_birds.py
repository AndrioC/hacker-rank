#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):

	bird_dict = {}

	for x in arr:
		if x in bird_dict:
			bird_dict[x] += 1
		else:
			bird_dict[x] = 1


	return (max(bird_dict.keys(), key = (lambda key: bird_dict[key])))			




arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)
print(result)

