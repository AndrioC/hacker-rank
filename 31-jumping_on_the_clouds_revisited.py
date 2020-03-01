#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):

	size = len(c)
	energy = 100
	i = k % size
	energy -= c[i] * 2 + 1
	while i != 0:
		i = (i + k) % size
		energy -= c[i] * 2 + 1

	return energy


	


nk = input().split()

n = int(nk[0])

k = int(nk[1])

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c, k)

print(result)
