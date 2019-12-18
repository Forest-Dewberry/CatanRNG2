# make a pseudorandom/not random at all number generator
# the order of the numbers chosen is somewhat random, but they are chosen as if
# out of a hat, so that each number is eventually chosen.
# for use with settlers of catan to eliminate randomness as a large consideration
# makes the game winner more strategy-dependent


# import
import numpy as np
import random as rand

global hat
global deck
global xvals
global hatsize
hatsize = 10
global ans
global randans


# define overarching objects
hat = []
deck = []

# define the distribution desired for outcomes of "rolls"
def distx(value):
	probx36 = abs(value-7)*(-1)*(1)+(6)
	return probx36

#* Populate Hat
# create a pool of outcomes
xvals =range(12-2+1)
for i in range(len(xvals)):
	xvals[i] +=2
# actually populate hat
for i in xvals:
	for j in range(distx(i)):
		hat.append(i)

print hat


def go():
	choices = range(len(hat))
	randidx = rand.choice(choices)
	randans = hat.pop(randidx)
	deck.append(randans)
	if len(hat) < hatsize:
		ans = deck.pop(0)
		hat.append(ans)
	return randans

def ff():
	myans = go()
	mylist.append(myans)
	plt.hist(mylist,bins=(12-2+1))
	plt.ylabel('No of times')
	plt.show()

