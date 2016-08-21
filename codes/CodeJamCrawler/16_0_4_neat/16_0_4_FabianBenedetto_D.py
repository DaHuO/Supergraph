import pdb; #pdb.set_trace()

# These functions print every possible position L can take IF there is only one L in K
# def position(K,C,i):
#     sum_list = [(i-1)*(K**(j)) for j in range(C)]
#     return sum(sum_list) + 1
#
# def all_positions(K,C):
#     pos_list = list()
#     for i in range(K):
#         pos_list.append(position(K,C,i+1))
#     return pos_list

def convert_to_position(coord,K):
    C = len(coord)
    sum_list = list()
    for i in range(C):
        if coord[i] > K: coord[i] = K
        sum_list.append((coord[i] - 1) * K**(C - (i+1)))
    return sum(sum_list) + 1

def tiles(K,C,S,case):
    K = int(K)
    C = int(C)
    S = int(S)
    coord_list = list()
    tiles_list = list()
    if C*S < K: return "Case #" + str(case) + ": IMPOSSIBLE"
    if K % C == 0:
        tries = K/C
    else:
        tries = K/C + 1
    for i in range(tries):
        temp_coords = list(range(1+i*C,1+(i+1)*C))
        coord_list.append(temp_coords)
    for element in coord_list:
        tiles_list.append(convert_to_position(element,K))
    returnstring = "Case #" + str(case) + ":"
    for digit in tiles_list:
        returnstring += " " + str(digit)
    return returnstring

t = int(raw_input())
for i in xrange(1, t + 1):
    K, C, S = [int(s) for s in raw_input().split(" ")]
    print tiles(K,C,S,i)
