def extsort(x):
	x.sort(key=lambda x:(x.split('.'))[1])
	return x

print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
	
