#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
	who_win = ''

	if abs(z-y) < abs(z-x):
		who_win = 'Cat B'
	elif abs(z-y) > abs(z-x):
		who_win = 'Cat A'
	else:
		who_win = 'Mouse C' 

	return who_win


q = int(input())

for q_itr in range(q):
    xyz = input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])

    result = catAndMouse(x, y, z)
    print(result)
