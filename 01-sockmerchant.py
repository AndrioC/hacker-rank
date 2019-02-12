'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, determine how many pairs of socks 
with matching colors there are.

For example, there arre n = 7 socks with colors ar = [1,2,1,2,1,3,2]. There is one pair of color 1 
and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.


-Function Description-
Complete the sockMerchant function. It must return an integer representing the number of matching pairs of socks
that are available.

sockMerchant has the following parameter(s):
-> n: the number of socks in the pile
-> ar: the colors of each sock


-Input Format-
The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.

-Constraints-

-> 1 <= n <= 100
-> 1 <= ar[i] <= 100 where 0 <= i < n

-Output Format-
Return the total number of matching pairs of socks that John can sell.

-Sample Input-
9
10 20 20 10 10 30 50 10 20

-Sample Output-
3

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	dict_socks = {}
	vals_socks = []

	for x in ar:
		if x in dict_socks:
			dict_socks[x] += 1
		else:
			dict_socks[x] = 1


	for k,v in dict_socks.items():
		vals_socks.append(v//2)

	return sum(vals_socks)




n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)
print(result)