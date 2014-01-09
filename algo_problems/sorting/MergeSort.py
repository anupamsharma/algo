a = [12,5,10,24,7,9,10]

def merge(s, e, m):
	if s>=e:
		return
	n1 = m-s + 1
	n2 =  e - m
        c1 = 0
        c2 = 0
        a1 = a[s:m+1]
        a2 = a[m+1:e+1]
	total = s
	print a1,a2
	while(True):
		if c1==n1 or c2==n2:
			break
		if a1[c1]<=a2[c2]:
			a[total] = a1[c1]
			c1 = c1 + 1	
		else:
			a[total] = a2[c2]
			c2 = c2 + 1
		total = total + 1

	if c1!=n1:
		print c1, total
		a[total:e+1] = a1[c1:]
	if c2!=n2:
		print c2, total
		a[total:e+1] = a2[c2:]

def mergesort(p, q):
	if p >= q:
		return
	m = (p+q)/2
	mergesort(p, m)
	mergesort(m+1, q)
	merge(p,q,m)
b = list(a)
mergesort(0, len(a)-1)
print a
print b
print a == b
b.sort()
print a == b

			
			
		
	
        
