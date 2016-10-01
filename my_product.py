def myproduct(x):
	product=1
	for i in x:
		product*=i
	return product

print myproduct([1,2,3,4])
