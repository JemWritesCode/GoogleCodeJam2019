#Passes Test Set1 && Test Set 2, but not TestSet3
import sys
sys.stdout.flush()

t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
	num = raw_input().split(" ")
	first = int(num[0]) - 1
	second = 1
	first = int(str(first).replace('4','3'))
	second = (int(num[0]) - int(first))
	print "Case #{}: {} {}".format(i, first, second)
