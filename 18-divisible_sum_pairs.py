#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):

	sum_count = 0

	for i in range(n):
		for j in range(n):
			if (i < j and (ar[i] + ar[j]) % k == 0):
				sum_count += 1


	return sum_count


nk = input().split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)
print(result)
