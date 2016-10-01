def Unique(x):
	uniq=[x[0]]
	for i in x:
		if(i in uniq):
			pass
		else:
			uniq.append(i)
	return uniq

print Unique([1, 2, 1, 3, 2, 5])
print Unique([1, 4,5,5,6,7,4,2,456,1, 3, 2, 5])


	
