def triplet(n):
	return [(x,y,x+y) for x in range(n) for y in range(n) if (x+y)<n]

print triplet(5)
	
