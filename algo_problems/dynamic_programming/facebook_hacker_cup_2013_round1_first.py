import sys

def get_input(fd):
    fd.readline()
    while(True):
        line = fd.readline().strip()
        if not line:
            break
        else:
            params = [int(i) for i in line.split(" ")]
            line = fd.readline().strip()
            in_array = [int(i) for i in line.split(" ")]
            yield (params[0], params[1], in_array)

NUMBER = 1000000007
in_count = 1

max =  10000 + 1
b_coeff = [range(0, max) for i in range(0, max) ]
b_coeff[0][0] = 1
b_coeff[1][1] = 1
b_coeff[1][0] = 1
for i in range(1, max):
    max_j = i
    b_coeff[i][0] = 1
    b_coeff[i][i] = 1
    for j in range(1, max_j):
        b_coeff[i][j] = b_coeff[i-1][j-1] + b_coeff[i-1][j]  
        b_coeff[i][j] = b_coeff[i][j] % NUMBER

for input_ds in get_input(sys.stdin):
   input_length = input_ds[0]
   k = input_ds[1]
   input_array = input_ds[2]
   input_array = sorted(input_array)
   count = k - 1
   total = 0

   while(count < input_length):
        value = input_array[count] % NUMBER
        try:
            contribution = (b_coeff[count][k-1] * value) % NUMBER
        except IndexError:
            print count, k-1
            exit()
        total = (total + contribution) % NUMBER
        total = total % NUMBER
        count = count + 1

   print "Case #" + str(in_count) + str(": ") + str(total % NUMBER) 
   in_count = in_count + 1
