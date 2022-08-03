def numbers(num):
		for y in range(0, num+1):
				for x in range(num - y, 0, -1):
						print(x, end=" ")
				print("")

numbers(5)