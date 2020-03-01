#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):

    sum_students = 0

    for x in a:
        if x <= 0:
            sum_students += 1

    if (sum_students < k):
        return 'YES'
    else:
        return 'NO'


t = int(input())

for t_itr in range(t):

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))

    result = angryProfessor(k, a)
    print(result)
