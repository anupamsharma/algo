def fastest_way(a, t, e, x, n):
	f = [range(0, n), range(0,n)]
	
	l = [range(0, n), range(0,n)]
	
	final_work_count = 0
	final_work_line = -1
	f[0][0] = e[0] + a[0][0]
	f[1][0] = e[1] + a[1][0]
	
	for j in range(1, n):
		if (f[0][j-1] + a[0][j]) < (f[1][j-1] +  t[1][j-1] + a[0][j]):
			 f[0][j] = f[0][j-1] + a[0][j]
			 l[0][j] = 0
		else:
			f[0][j] = f[1][j-1] +  t[1][j-1] + a[0][j]
			l[0][j] = 1
	
		if (f[1][j-1] + a[1][j]) < (f[0][j-1] + t[0][j-1] + a[1][j]):
			 f[1][j] = f[1][j-1] + a[1][j]
			 l[1][j] = 1
		else:
			f[1][j] = f[0][j-1] + t[0][j-1] + a[1][j]
			l[1][j] = 0

	if f[0][n-1] + x[0] < f[1][n-1] + x[1]:
		final_work_count = f[0][n-1] + x[0]
		final_work_line = 0
	else:
		final_work_count = f[1][n-1] + x[1]
		final_work_line = 1
	return (final_work_count, final_work_line, l)

def print_path(l, final_work_line, n):
	line = final_work_line
	print "Line is %s for station %s "  % (str(line), str(n-1))
	for j in range(n-1, 0, -1):
		line = l[line][j]
		print "Line is %s for station %s "  % (str(line), str(j-1))

e = (2, 4)
a = ((7,9,3,4,8,4), (8,5,6,4,5,7))
x = (3, 2)
t = ((2,3,1,3,4), (2,1,2,2,1))

n = 6
(final_work_count, final_work_line, l) = fastest_way(a, t, e, x, n)
print "Cost through cheapest path ", final_work_count, 

print "\n====================\n\nPath in reverse order is => \n "
print_path(l, final_work_line, n)
