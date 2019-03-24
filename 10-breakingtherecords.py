#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    
    count_max = 0
    count_min = 0


    break_value = scores[0]
    worst_value = scores[0]
    for x in range(len(scores)-1):
        if (scores[x+1] > scores[x] and scores[x+1] > break_value):
            count_max += 1
            break_value = scores[x+1]
        elif (scores[x+1] < scores[x] and scores[x+1] < worst_value):
            count_min += 1
            worst_value = scores[x+1]

    return (count_max, count_min)


n = int(input())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

print(result)

