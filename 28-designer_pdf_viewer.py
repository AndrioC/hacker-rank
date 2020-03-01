#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):

	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w', 'x', 'y', 'z']
	pos_alpha = []
	tallest_pos = []

	for x in range(len(word)):
		pos_alpha.append(alphabet.index(word[x])+1)

	for x in pos_alpha:
		tallest_pos.append(h[x-1])

	selection_area = len(word) * 1 * max(tallest_pos)

	return selection_area




h = list(map(int, input().rstrip().split()))

word = input()

result = designerPdfViewer(h, word)

print(result)

