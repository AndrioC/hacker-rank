#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):

	max_hurdle = max(height)
	min_doses = 0

	if max_hurdle >= k:
		min_doses = abs(max_hurdle - k)
		return min_doses

	return min_doses





nk = input().split()

n = int(nk[0])

k = int(nk[1])

height = list(map(int, input().rstrip().split()))

result = hurdleRace(k, height)

print(result)