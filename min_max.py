def Min(x):
	i=0
	minimum=x[i]
	while(i<len(x)):
		if(x[i]<minimum):
			minimum=x[i]
			i+=1
		else:
			i+=1	
	return minimum

def Max(x):
        i=0
        maximum=x[i]
        while(i<len(x)):
                if(x[i]>maximum):
                        maximum=x[i]
                        i+=1
                else:
                        i+=1
        return maximum

print Min([2,1,3,4])
print Min(['abc','pqr','xyz'])
print Max([2,3,4,5,4564,74675,7345,74676])
