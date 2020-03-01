#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input())

list_consec_sum = []
bin_convert = str(bin(n)[2:]).split('0')

for x in bin_convert:
	list_consec_sum.append(len(x))

print(max(list_consec_sum))

