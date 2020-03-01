# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
	new_position_apples = list(map(lambda x:x+a, apples))
	new_position_oranges = list(map(lambda x:x+b, oranges))

	number_apples = 0
	number_oranges = 0

	for x in new_position_apples:
		if x >= s and x <= t:
			number_apples += 1



	for x in new_position_oranges:
		if x >= s and x <= t:
			number_oranges += 1

	print(number_apples)
	print(number_oranges)

st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)

