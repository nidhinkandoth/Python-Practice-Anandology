def cumulative_product(x):
	temp=1
	p=[]
	for i in x:
		temp*=i
		p.append(temp)
	return p

print cumulative_product([1, 2, 3, 4])
print cumulative_product([4, 3, 2, 1])
