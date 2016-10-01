def Reverse(x):
	i=-1
	revx=[]
	while(i>=(-len(x))):
		revx.append(x[i])	 
		i-=1
	return revx
print Reverse([1,2,3,4,5,6])
print Reverse(['a','b','c','d'])
print Reverse([9,8,7,6,5,4,3,2,1,0])
		
