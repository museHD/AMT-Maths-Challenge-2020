from itertools import permutations
import itertools
from operator import itemgetter

rooms = [1,2,3,4,5,6,7,8,9,10]


def FiveAB():

	x = list(permutations(rooms, 2))

	print(len(x))


	difflist = []

	count = 0 
	for i in x:
		difflist.append(abs(i[0]-i[1])) # Calculate difference between rooms
		count += 1

	total = 0
	print("Number of rooms separating them: ")
	for l in range(10):
		print(str(l) + ": " + str(difflist.count(l)))
		total += difflist.count(l)

	print("Total number of rooms: " + str(total))
	print("Chance of ONE room separating them: " + str(18/total*100))
	print("Polly is correct.")
	print()
	print()
def FiveC():

	x = list(permutations(rooms,3))
	newlist = []
	for i in x:
		sortlist = sorted(i)
		newlist.append(sortlist)

	print("Total number of permutations of rooms: " + str(len(newlist)))

	conseclist = []
	for j in newlist:
		if (((j[2] - j[1]) + (j[1] - j[0]))) <= 4:
			conseclist.append(j)
	print("Number of permutations for 5 consecutive rooms: " + str(len(conseclist)))
	print("Chance that the are within a block of 5 consecutive rooms: " + str(len(conseclist)/len(x)*100) + "%")
	print("Therefore, Ollie is correct")

smallrooms = [1,2,3,4,5]
x = list(permutations([1,2,3,4,5], 2))
for i in x:
	print(i)
	i = set(i)

print(len(x))
