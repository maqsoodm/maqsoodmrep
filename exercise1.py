count = 0
for i in range(2000, 3200):
	if (i%5) != 0 and (i%7) == 0:
		print(str(i) + ",", end=" ")
		count = count+1
print(count)