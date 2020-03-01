#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
	size = len(p)
	cres_list = p
	p_sorted = sorted(p)
	index_list = []
	element_list = []

	for x in range(size):
		index_list.append(cres_list.index(p_sorted[x]) + 1)
		element_list.append(cres_list.index(index_list[x]) + 1)


	return element_list

n = int(input())

p = list(map(int, input().rstrip().split()))

result = permutationEquation(p)

print(result)
