# Incomplete - I didn't finish in time.
# Need to read up on what numpy does--kept seeing tutorials say to use it for arrays?
# [:] used for copy whole array  with Slice Notation


import sys
import numpy as np
sys.stdout.flush()

t = int(raw_input()) # read a line with a single integer (first number typed)
for i in xrange(1, t + 1):
	case = raw_input().split(" ") # gets the 2 integers for R and C
	rows = int(case[0])
	columns = int(case[1])
	if rows * columns > 4 and rows * columns % 2 == 0:
		print "Case #{}: {}".format(i, "POSSIBLE")
		visited = []
		position = [2, 3] #starting position
		for i in range(1, rows * columns): #for the number of blocks in the grid.
			#if position in visited:
				position[0] += 2
				position[1] += 2
				print position
			
				visited.append(position[:]) #slice the array to get the copy instead of pointer.

				print "visited is: "
				print visited

		
		
					
	else:
		print "Case #{}: {}".format(i, "IMPOSSIBLE")


	
	
