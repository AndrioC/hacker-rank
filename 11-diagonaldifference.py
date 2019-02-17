'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9


The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15 - 17| = 2.


-Function Description-

Complete the diagonalDifference function in the editor below. It must return an integer representing the absolute diagonal difference.

diagonalDifference takes the following parameter:

-> arr: an array of integers .

-Input Format-

The first line contains a single integer, n, the number of rows and columns in the matrix arr. 
Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

-Constraints-

-> -100 <= arrr[i][j] <= 100

-Output Format-

Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

-Sample Input-

3
11 2 4
4 5 6
10 8 -12

-Sample Output-

15

-Explanation-

The primary diagonal is:

11
   5
     -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10

Sum across the secondary diagonal: 4 + 5 + 10 = 19 
Difference: |4 - 19| = 15

'''






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

