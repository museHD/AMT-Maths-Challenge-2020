from itertools import *
import itertools
x 
# def sinkable(seq):

# 	holes = [1,2,3,4,5]

# 	for i in range(4):
# 		if seq[i]



lst = [1, 2, 3, 4, 5]
x = [p for p in itertools.product(lst, repeat=5)]


print(len(x))
counter = 0	
for i in x:
	if 4 in i or 5 in i:
		if i.count(4) ==1 and i.count(5) ==1 and i.count(3) <= 2 and i.count(2) <= 3 and i.count(1) >= 1:
			print(i)
			counter += 1

print(counter)

#5: 685
#4 and 5: 380  



