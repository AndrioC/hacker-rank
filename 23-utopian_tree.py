#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):

	h_sum = 0

	for x in range(0,n+1):
		if x == 0:
			h_sum = 1
		elif x % 2 == 0 and x != 0:
			h_sum += 1
		else:
			h_sum = h_sum * 2
	print(h_sum)		



t = int(input())

for t_itr in range(t):
    n = int(input())

    result = utopianTree(n)
