#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):

    #Don't do rotations. The algorithm is gonna get very slow for large tests
    rotation = [0] * len(a)
    size = len(a)

    for x in range(len(a)):
        rotation[(x+k) % size] = a[x] 


    return [rotation[i] for i in queries]

nkq = input().split()

n = int(nkq[0])

k = int(nkq[1])

q = int(nkq[2])

a = list(map(int, input().rstrip().split()))

queries = []

for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)

result = circularArrayRotation(a, k, queries)
print(result)