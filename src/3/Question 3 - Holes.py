from itertools import *
import itertools

# def sinkable(seq):

# 	holes = [1,2,3,4,5]

# 	for i in range(4):
# 		if seq[i]


# ABCD 
lst = [1, 2, 3, 4, 5]
x = [p for p in itertools.product(lst, repeat=5)]


# print(len(x))
counter = 0	
for i in x:
	if 4 in i or 5 in i:
		if i.count(4) ==1 and i.count(5) ==1 and i.count(3) <= 2 and i.count(2) <= 3 and i.count(1) >= 1:
			# print(i)
			counter += 1

# print(counter)
print("Question 1:")
print("----------------------------")
print("C:")
print("If there is only one 5-ball OR only one 4-ball, the number of sinkable sequences is 685.")
print()
print()
print("D:")

print("If there is at least one 4-ball and one 5-ball in the sequence, the number of possible sinkable sequences is 380")
#5: 685
#4 and 5: 380  
exit = input("Press ENTER to exit...")


