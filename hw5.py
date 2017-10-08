import re
hand = open('regex_sum_39558.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('[0-9]+', line)
	numlist.extend(stuff)

print (sum(map(int, numlist)))