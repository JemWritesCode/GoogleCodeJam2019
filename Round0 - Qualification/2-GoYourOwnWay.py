t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
	squareSize = raw_input().split(" ")
	LydiaPath = raw_input().split(" ") # read a list of integers, 2 in this case
	LydiaPath = ''.join(LydiaPath)
	myPath = LydiaPath.replace('S', '1')
	myPath = myPath.replace('E', 'S')
	myPath = myPath.replace('1', 'E')
	print "Case #{}: {}".format(i, myPath)
 