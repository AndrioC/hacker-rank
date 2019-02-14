'''
Monica wants to buy a keyboard and a USB drive from her favorite eletronics store. The store
has several models of each. Monica wants to spend as much as possible for the 2 items, given her budget.

Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the 
amount of money Monica will spend. If she doesn't have enough money to both a keyboard and a USB drive,
print -1 instead. She will buy only the two required items.

For example, suppose she has b = 60 to spend. Three types of keyboards cost keyboards = [50,50,60]. Two USB
drives cost drives = [5,8,12]. She could purchase a 40 keyboard + 12 USB DRIVE = 52, or a 50 keyboard + USB drive = 58.
She chooses de latter. She can't buy more than 2 items so she can't spend exacly 60.

-Function Description-
Complete the getMoneySpent function in the editor below. It should return the maximum total price for the two items within Monica's budget,
or -1 if she cannot affort both items.

getMoneySpent has the following parameter(s):

-> keyboards: an array of integers representing keyboard prices
-> drives: an array of integers representing drive prices
-> b: the units of currency in Monica's budget


-Input Format-

-> The first line contains three space-separated integers b, n, and m, her budget, the number of keyboard models and the number of 
USB drive models. 
-> The second line contains n space-separated integers keyboard[i], the prices of each keyboard model. 
-> The third line contains m space-separated integers drives,the prices of the USB drives.

-Constraints-

-> 1 <= n,m <= 100
-> 1 <= b <= 10^6
-> The price of each item is in the inclusive range [1,10^6]

-Output Format-
Print a single integer denoting the amount of money Monica will spend. If she doesn't have enough 
money to buy one keyboard and one USB drive, print -1 instead.

-Sample Input-
10 2 3
3 1
5 2 8

-Sample Output-
9

-Explanation-

She can buy the second keyboard and the third USB drive for a total cost of 8 + 1 = 9

-Sample Input 1-
5 1 1
4
5

-Sample Output 1-
-1

-Explanation 1-

There is no way to boy one keyboard and one USB drive because 4 + 5 > 5, so we print -1.
'''

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