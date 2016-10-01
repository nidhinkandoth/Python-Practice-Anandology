def group(x,i):
	splitted=[]
	j=0
	while(j<len(x)):
		splitted.append(x[j:i])
		j=i
		i=i+i
	return splitted

print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)

