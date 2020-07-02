from itertools import permutations
# import numpy as np
def OneCD():
	print("Question 1 C & D")
	print("-------------------")
	l1=[]
	print("Trying every value till 100 for a 16 chunk rectangle using derived formula")
	for val in range(100):
		sum = (16 * val) + 136
		l1.append(sum/16)

	print()
	l2=[]

	print("Trying every value till 100 for a 15 chunk rectangle using derived formula")
	print()

	for val in range(100):
		sum = (15 * val) + 180
		l2.append(sum/15)

	print("15-Chunk Quotient        16-Chunk Quotient")
	for i in range(99):
		print("     " + str(l2[i]) + "                    " + str(l1[i]))

	d = {'16-Chunk':l1,'15-Chunk':l2}
	# df = pd.DataFrame(d, columns=['15-Chunk','16-Chunk'])
	# print(df)
	# Broken For PyInstaller ^^^

	print()
	print("As you can see, every quotient for the 15-Chunk is a whole value, meaning that x is\ndivisible by 15 whereas every single quotient for the 16-Chunk is a Decimal number meaning that x the number is not fully divisible by 16.")


def OneA():
	counter = 0

	x = list(permutations(range(50,70),8))
	for item in x:
		print(item)
		total = 0
		for num in item:
			num += total
		if total == 600:
			print(item)
			break
	print('no item :(')
		
		# print(counter)
	

def isAdjacent(x,y):
	top = x - 10
	bottom = x + 10
	left = x -1
	right = x+1
	if (y == top) or (y == bottom) or (y == left) or (y == right):
		return True
	else:
		return False

# unittest = permutations(range(0,9),8)
# for i in unittest:
# 	total = 0
# 	for l in i:
# 		total = total + l
# 	# print(total)
# 	total = str(total)
# 	if total[-1] == "0":
# 		print(i)

OneCD()
leave = input("Press ENTER to exit...")