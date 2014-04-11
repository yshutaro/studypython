import math
def checkio(ls):
	ls.sort()
	print "start"
	if len(ls) % 2 != 0:
		return ls[int(math.floor(len(ls) / 2))] 
	else:
		return (float(ls[(len(ls) / 2) -1 ] + ls[len(ls) / 2])) / 2

if __name__ == "__main__":

	print checkio([1, 2, 3, 4, 5])
	print checkio([3, 1, 2, 5, 3])
	print checkio([1, 300, 2, 200, 1])
	print checkio([3, 6, 20, 99, 10, 15])
