#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):

	cumulative = 0
	shared = 0
	liked = 0

	for x in range(1, n+1):
		if x == 1:
			cumulative = 2
			shared = 5
			liked = 2
		else:
			#Round doesn't work right. It rounds up in some cases
			shared = int(shared/2) * 3
			liked  = int(shared/2)
			cumulative += liked
	return(cumulative)

n = int(input())

result = viralAdvertising(n)

print(result)
