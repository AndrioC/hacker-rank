def kangaroo(x1, v1, x2, v2):

	d = 10000
	new_x1 = x1
	new_x2 = x2
	answer = 'NO'

	for x in range(d):

		if (new_x1 == new_x2):
			answer = 'YES'
			break
		else:			
			new_x1 += v1
			new_x2 += v2
	return answer

x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)
print(result)
