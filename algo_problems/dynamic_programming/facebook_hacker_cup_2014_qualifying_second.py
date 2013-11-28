#/usr/local/bin/python
import sys
import heapq
def convert_to_list(in_str):
# We do not need to convert it to bitstring as max input size is small.
    return in_str

def get_curr_p(n, m, p, players):
    # even team
    if 2 * p == n:
        return sorted([i[-1] for i in players])
    
    even_team =  players[1::2]
    odd_team = players[0::2]
    even_team_constant = False
    odd_team_constant = False
    if len(even_team) == p:
        even_team_constant = True
    if len(odd_team) == p:
        odd_team_constant = True
    even_playing = [[-i[0], -i[1], i[2]] for i in even_team[0:p]]
    odd_playing =  [[-i[0], -i[1], i[2]] for i in  odd_team[0:p]]
    heapq.heapify(even_playing)
    heapq.heapify(odd_playing)

    even_seating = even_team[p:]
    odd_seating = odd_team[p:]
    heapq.heapify(even_seating)
    heapq.heapify(odd_seating)

    count = 1

    while(count <= m):
       if not even_team_constant:
            for i in even_playing:
                i[0] = i[0] - 1
            in_pl = heapq.heappop(even_seating)
            in_pl = [-in_pl[0], -in_pl[1], in_pl[2]]
            out_pl = heapq.heappop(even_playing)
            out_pl = [-out_pl[0], -out_pl[1], out_pl[2]]
            heapq.heappush(even_playing, in_pl)
            heapq.heappush(even_seating, out_pl)
       if not odd_team_constant:
            for i in odd_playing:
                i[0] = i[0] - 1
            in_pl = heapq.heappop(odd_seating)
            in_pl = [-in_pl[0], -in_pl[1], in_pl[2]]
            out_pl = heapq.heappop(odd_playing)
            out_pl = [-out_pl[0], -out_pl[1], out_pl[2]]
            heapq.heappush(odd_playing, in_pl)
            heapq.heappush(odd_seating, out_pl)
       count  = count + 1
    return sorted([i[-1] for i in (even_playing + odd_playing)])
    #if 2 * p == n:
    #    return players
    #else:
        
def get_proper_ds(in_ds):
    player_list = [[0, 0, i[0]]  for i in sorted(in_ds[-1], key=lambda x: (x[1], x[2]))]
    player_list.reverse()
    count = 0
    length = len(player_list)
    while(count < length):
        player_list[count][1] = count
        count = count + 1
    return player_list
 
def get_test_inputs(fd):
    no_of_test_cases = 0
    current_test_case = 0
    line_number = 2
    current_test_case = []
    current_test_case_start = 2
    no_of_test_cases == int(fd.readline().strip())
    params = [int(i) for i in fd.readline().strip().split()]
    current_test_case_size = params[0]
    while(True):
        line = fd.readline().strip()
        if not line:
            break
        else:
            if line_number < current_test_case_start + current_test_case_size - 1:
                l_p = line.strip().split()
                current_test_case.append([l_p[0], int(l_p[1]), int(l_p[2]) ])
            elif line_number > current_test_case_start + current_test_case_size - 1:
                current_test_case = []
                current_test_case_start = line_number + 1
                params = [int(i) for i in line.split()]
                current_test_case_size = params[0]
            else:
                l_p = line.split()
                current_test_case.append([l_p[0], int(l_p[1]), int(l_p[2]) ])
                yield (params, current_test_case)
        line_number = line_number + 1
count = 1
for ds in get_test_inputs(sys.stdin):
    print "Case #" + str(count) + ": " + " ".join(get_curr_p(ds[0][0], ds[0][1], ds[0][2], get_proper_ds(ds)))
    count = count + 1
