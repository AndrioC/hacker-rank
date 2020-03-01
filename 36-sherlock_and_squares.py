#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    total = 0
    for x in range(math.ceil(math.sqrt(a)), b):
        if math.pow (x,2) <= b:
            total += 1
        else:
            break
    return total


q = int(input())

for q_itr in range(q):
    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    result = squares(a, b)
    print(result)

