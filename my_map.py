def my_map(f,x):
	result=[]
	for i in x:
		result.append(f(i))
	return result


print my_map(lambda x:x*x,[1,2,3,4,5])

