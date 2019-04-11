t = int(raw_input())
for i in xrange(1, t + 1):
	squareSize = raw_input().split(" ")
	LydiaPath = raw_input().split(" ")
	LydiaPath = ''.join(LydiaPath)
	myPath = LydiaPath.replace('S', '1')
	myPath = myPath.replace('E', 'S')
	myPath = myPath.replace('1', 'E')
	print "Case #{}: {}".format(i, myPath)
 
