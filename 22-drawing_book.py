#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def getIndexItem(listToFind, number):
	for i in range(len(listToFind)):
		if number in listToFind[i]:
			return (i, listToFind[i].index(number))   


def pageCount(n, p):
	x1 = []
	list_book = []
	list_diff = []

	for x in range(1,n):
		x1 = []
		if n % 2 == 0:
			if x != 1 and x %2 == 0 and x != n:
				x1.append(x)
				x1.append(x+1)
				list_book.append(x1)
		elif n % 2 != 0:
			if x != 1 and x % 2 == 0:
				x1.append(x)
				x1.append(x+1)
				list_book.append(x1)

	if n % 2 == 0:
		list_book.insert(0, [1])
		list_book.append([n])		
	else:
		list_book.insert(0, [1])

	#Page to turn to
	x1 = getIndexItem(list_book, p)[0]

	#First page
	x2 = getIndexItem(list_book, 1)[0]

	#Last page
	x3 = getIndexItem(list_book, n)[0]

	#Difference and put them into a list
	list_diff.append(abs(x2-x1))
	list_diff.append(x3-x1)


	print(min(list_diff))
	


n = int(input())

p = int(input())

result = pageCount(n, p)