def LenSort(x):
	x.sort(key=lambda y:len(y))
	return x
	

print LenSort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
