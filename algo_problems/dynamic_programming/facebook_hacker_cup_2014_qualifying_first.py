#/usr/local/bin/python
import sys

def convert_to_list(in_str):
# We do not need to convert it to bitstring as max input size is small.
    return in_str

def get_test_inputs(fd):
    no_of_test_cases = 0
    current_test_case = 0
    current_day = 0
    line_number = 2
    current_test_case = []
    current_test_case_start = 2
    no_of_test_cases == int(fd.readline().strip())
    current_test_case_size = int(fd.readline().strip())
    while(True):
        line = fd.readline().strip()
        if not line:
            break
        else:
            if line_number < current_test_case_start + current_test_case_size - 1:
                current_test_case.append(convert_to_list(line))
            elif line_number > current_test_case_start + current_test_case_size - 1:
                current_test_case = []
                current_test_case_start = line_number + 1
                current_test_case_size = int(line)
            else:
                current_test_case.append(convert_to_list(line))
                yield current_test_case
        line_number = line_number + 1

    
def get_sq_dim(x):
    if x[x.find("#") : x.rfind("#") + 1].find(".") == -1:
       return x.rfind("#") - x.find("#") + 1
    return None

def if_sq(in_sq, counter):
    all_whites = WHITE * len(in_sq[0])
    res = True
    row_no = 0
    sq_not_started = True
    for row in in_sq:
        if sq_not_started:
            if all_whites == row:
                continue

            sq_size = get_sq_dim(row) 
            if sq_size:
                sq_not_started = False
                sq_start = row_no
                sq_start_row = row
            else:   
                res = False
                break
        else:
             if row_no < sq_start + sq_size:
               
                if row != sq_start_row:
                    res = False
                    break   
             else:
                if all_whites != row:
                    res = False
                    break
        row_no = row_no + 1
    return res and (not sq_not_started)            

BLACK = "#"
WHITE = "."
count = 1
for in_sq in get_test_inputs(sys.stdin):
    res = if_sq(in_sq, count)
    if res == True: 
       print "Case #" + str(count) + ": YES"
    else:
       print "Case #" + str(count) + ": NO"
    count = count + 1
