def square(x):
	return x*x
def fxy(f,x,y):
	return f(x)+f(y)

print fxy(square,2,3)
