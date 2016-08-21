import itertools

T = int(raw_input())

def get_max_index(dic):
    if all_zero(dic):
        return None
    max_item = None
    max_index = None
    for key,item in dic.items():
        if max_item < item:
            max_item = item
            max_index = key
    return max_index

def all_zero(dic):
    #print dic
    for key,item in dic.items():
        if item != 0:
            return False

    return True

def total_three(dic):
    total = 0
    for key,item in dic.items():
        total += item
        if total > 3 or item > 1:
            return False

    if total == 3:
        return True
    else:
        return False

def get_ones(dic):
    answer = []
    for key,item in dic.items():
        if item == 1:
            answer.append(key)

    return answer


for i in range(T):
    print "Case #" + str(i+1) + ":",
    N = int(raw_input())
    P = {}

    tmp = map(int, raw_input().split(' '))

    for j in range(N):
        P[j] = tmp[j]

    #print P
    while not all_zero(P):
        if(total_three(P)):
            u, v, w = get_ones(P)
            print chr(ord('A') + u), chr(ord('A') + v) + chr(ord('A') + w),
            break;
        max_index = get_max_index(P)
        #print max_index
        first_char = chr(ord('A') + max_index)
        P[max_index] -= 1
        sec_max_index = get_max_index(P)
        if sec_max_index is None:
            print first_char,
        else:
            second_char = chr(ord('A') + sec_max_index)
            P[sec_max_index] -= 1
            print first_char + second_char,

    print ""

    


