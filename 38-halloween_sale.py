#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy

    new_value = p
    new_p = p
    sum_games = 0

    while new_value <= s:
        new_p -= d
        if new_p <= m:
            new_value += m
        else: 
            new_value += new_p
        sum_games += 1

    return sum_games


pdms = input().split()

p = int(pdms[0])

d = int(pdms[1])

m = int(pdms[2])

s = int(pdms[3])

answer = howManyGames(p, d, m, s)

print(answer)