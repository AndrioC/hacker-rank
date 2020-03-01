#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	dict_socks = {}
	vals_socks = []
	
	for x in ar:
		if x in dict_socks:
			dict_socks[x] += 1
		else:
			dict_socks[x] = 1


	for k,v in dict_socks.items():
		vals_socks.append(v//2)

	return sum(vals_socks)

n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)
print(result)
