from itertools import permutations

a = "a"
b = "b"

binary=[a,b]
import itertools


# print (combos)

def generateStrings(length, constantstr=""):
	output = []
	for i in itertools.product(binary, repeat=length):
		c = (''.join(map(str, i)))
		d = (constantstr + c)
		output.append(d)
	return output

# Returns True or False according to whether a string is a palindrome or not
def isPd(word):
	reverse = word [::-1]
	if (word == reverse):
		print(word)
		return True
		
	else:
		# print("no")
		return False
		
# Counts the number of palindromes in a list 
def countPs(words):
	counter = 0
	for word in words:
		if isPd(word):
			counter += 1
		else:
			pass
	print("Palindromic Substrings: " + str(counter))
	print()
	print("-------------------------")
	print()

	return counter

# Goes through the words and picks out each substring; counts each palindromic substring found
def getSubstrs(words):
	for ix, string in enumerate(words):
		print("WORD:" + str(ix+1))
		print(string)
		print("Palindromic: ")
		substrings = [string[x:y] for x, y in itertools.combinations( range(len(string) + 1), r = 2)] 
		substrings = set(substrings)
		countPs(substrings)


def TwoD():
	combos = []
	givenstr = "aabba"
	combos = generateStrings(3,givenstr)
	getSubstrs(combos)


def TwoC():
	combos = []
	combos = generateStrings(5)
	getSubstrs(combos)

def TwoB():
	combos = []
	combos = generateStrings(4)
	getSubstrs(combos)

def TwoA():
	combos = generateStrings(3)
	getSubstrs(combos)

TwoA()