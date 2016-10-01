def cumulative_sum(x):
	c=[]
	temp=0
	for i in x:
		temp+=i
		c.append(temp)
	return c

print cumulative_sum([1,2,3,4])
print cumulative_sum([4,3,2,1])	
		
