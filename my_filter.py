def my_filter(f,a):
	filtered=[]
	for i in a:
		if(f(i)==True):
			filtered.append(i)
		else:
			pass
	return filtered	

print my_filter(lambda x:x%2==0,range(11))
