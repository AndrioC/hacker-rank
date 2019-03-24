#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
	sum_dia_1 = 0
	sum_dia_2 = 0

	max_value = max(list(range(len(arr))))
	size = len(arr)

	#Crazy, bruh!
	for i in range(len(arr)):
		for j in range(len(arr)):
			#Matrices with size 2,4,6,8,10...
			if (size%2 == 0):
				#All values from the left diagonal
				if i == j:
					sum_dia_1 += arr[i][j]
				#Getting all elements from the right diagonal
				#We escalate from 0 until the last value of the loop, using i
				#We escalate from the last value until 0, using j
				#Like this way: With a matrix 4x4:[i = 0, j = 4], [i = 1, j = 3], [i = 2, j = 2], [i = 3, j = 1], [i = 4, j = 0]
				elif (i == i and j == max_value-i):
					sum_dia_2 += arr[i][j]	
			#Matrices with size 3,5,7,9,11...	
			else:
				#All values from the left diagonal, except the value when i is equal to j and the difference between max_value and i and the 
				#difference between max_value is i and j itself. Example: With a matrix 3x3: The max_value is 2 (index starts at 0). 
				#So we have: [0,0], but 2 (max_value) - 0 is different from zero, and 2 - 0 is also different from zero. 
				#We also have [1,1], and 2 - 1 = 1 and 2 - 1 = 1, so we don't collect the element from [1,1]
				if i == j and (i != max_value-i and j!= max_value-j):
					sum_dia_1 += arr[i][j]
				#Now, if the value of i and j are equals to max_value-i, then i can add to the two sums. It's the element that we exclude above.
				elif (i == max_value-i and j == max_value-i):
					sum_dia_1 += arr[i][j]
					sum_dia_2 += arr[i][j]
				#Finally, all the elements from the right diagonal	
				elif (i == i and j == max_value-i):
					sum_dia_2 += arr[i][j]
	
	print(abs(sum_dia_1-sum_dia_2))

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

