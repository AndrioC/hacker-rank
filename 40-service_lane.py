#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases, width, t):

    temp_list = []
    def_list = []


    for x in range(0,t):
        min_range = cases[x][0]
        max_range = cases[x][1]

        for y in range(min_range, max_range+1):
            temp_list.append(width[y])
        def_list.append(min(temp_list))
        temp_list = []
    
    return def_list

nt = input().split()

n = int(nt[0])

t = int(nt[1])

width = list(map(int, input().rstrip().split()))

cases = []

for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))

result = serviceLane(n, cases, width, t)

print(result)