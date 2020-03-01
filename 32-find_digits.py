#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):

	number = n
	count_div = 0
	list_digits = str(n)

	for x in range(len(list_digits)):
		if int(list_digits[x]) != 0 and number % int(list_digits[x]) == 0: 
			count_div += 1
		else:
			pass

	return count_div


t = int(input())

for t_itr in range(t):

    n = int(input())

    result = findDigits(n)

    print(result)

