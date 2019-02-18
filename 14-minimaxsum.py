'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as 
a single line of two space-separated long integers.

For example, arr = [1,3,5,7,9]. Our minimum sum is 1 + 3 + 5 + 7 = 16 and our maximum sum is 3 + 5 + 7 + 9 = 24. We would print:

16 24


-Function Description-

Complete the miniMaxSum function in the editor below. It should print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

miniMaxSum has the following parameter(s):

-> arr: an array of 5 integers

-Input Format-

A single line of five space-separated integers.

-> 1 <= arr[i] <= 10^9

-Output Format-

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. 
(The output can be greater than a 32 bit integer.)

-Sample Input-

1 2 3 4 5

-Sample Output-

10 14


-Explanation-

Our initial numbers are 1, 2, 3, 4, and 5. We can calculate the following sums using four of the five integers:

-> If we sum everything except 1, our sum is 2 + 3 + 4 + 5 = 14.
-> If we sum everything except 2, our sum is 1 + 3 + 4 + 5 = 13.
-> If we sum everything except 3, our sum is 1 + 2 + 4 + 5 = 12.
-> If we sum everything except 4, our sum is 1 + 2 + 3 + 5 = 11.
-> If we sum everything except 5, our sum is 1 + 2 + 3 + 4 = 10.

'''



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

	sum_total = 0
	operations_list = []

	for x in arr:
		sum_total += x

	for x in arr:
		operations_list.append(sum_total - x)

	print(min(operations_list), max(operations_list))


arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)
