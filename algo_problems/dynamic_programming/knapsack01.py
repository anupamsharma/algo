s = [10,20,30]
v = [60,100,120]
W = 50
M = 3
res = [[0 for j in range(0, W+1)] for i in range(0, M)]

for w in range(0, W+1):
	if s[0] <= w:
		res[0][w] = v[0] 
	for m in range(1, M):
		if w-s[m]>=0:
			res[m][w] = max(v[m] + res[m-1][w-s[m]], res[m-1][w])

	
print res[2][50]
