#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):

	new_bill = [x for i,x in enumerate(bill) if i != k]
	sum_check = sum(new_bill)

	if (b > (sum_check/2)):
		print(int(b-(sum_check/2)))
	else:
		print("Bon Appetit")


nk = input().rstrip().split()

n = int(nk[0])

k = int(nk[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)