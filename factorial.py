def myproduct(x):
	product=1
	for i in x:
		product*=i
	return product

def my_fact(x):
	a=range(1,x+1)
	return myproduct((a))

print my_fact(4)
print my_fact(5)
print my_fact(6)
print my_fact(7)
