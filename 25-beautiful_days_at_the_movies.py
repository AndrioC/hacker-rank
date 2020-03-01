#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):

	num_days = 0

	for x in range(i, j+1):
		new_i = int(str(x)[::-1])

		if (abs(x-new_i)) % k == 0:
			num_days += 1

	return(num_days)



ijk = input().split()

i = int(ijk[0])

j = int(ijk[1])

k = int(ijk[2])

result = beautifulDays(i, j, k)

print(result)