import hdc
def f():
	return hdc.go(), hdc.hat, hdc.deck

if __name__ == '__main__':
	import random as r
	import matplotlib.pyplot as plt
	vals = []
	for i in range(50):
		vals.append(hdc.go())
	print ''
	print 'die rolls with CatanRNG2:'
	print vals
	print ''
	plt.hist(vals, bins=11)
	plt.show(block=False)
	plt.pause(3)
	vals2 = []
	die = [1,2,3,4,5,6]
	for i in range(50):
		vals2.append(r.choice(die)+r.choice(die))
	print 'die rolls with normal dice:'
	print vals2
	plt.hist(vals2, bins = 11)
	plt.show()

