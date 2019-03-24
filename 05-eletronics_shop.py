#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):

	sum_usb_keyboard = []

	for x in range(len(keyboards)):
		for k in range(len(drives)):
			temp_sum = keyboards[x] + drives[k]
			if (temp_sum) <= b:				
				sum_usb_keyboard.append(temp_sum)
			else:
				sum_usb_keyboard.append(-1)

	return max(sum_usb_keyboard)  

bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

drives = list(map(int, input().rstrip().split()))

moneySpent = getMoneySpent(keyboards, drives, b)

print(moneySpent)
