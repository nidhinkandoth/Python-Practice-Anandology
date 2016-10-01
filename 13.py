#to check whether two strings are equal,ignoring case

def istrcmp(a,b):
	c=a.lower()
	d=b.lower()
	if(len(c)==len(d)):
		count=0
		for i in range(len(c)):
			if(c[i]==d[i]):
				count+=1
		return(count==len(c))
	else:
		return False
print istrcmp('abcd','abcd')
		
		
