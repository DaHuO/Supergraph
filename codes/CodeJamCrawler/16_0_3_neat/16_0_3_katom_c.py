import math

T = int(raw_input())

def find_divisor(N):
    for i in range(2, int(math.sqrt(N))):
        if(N % i == 0):
            return i

    return -1


def value_in_base(s, b):
    answer = 0
    s = s[::-1]
    for i,c in enumerate(s):
        if(s[i] == '1'):
            answer += b ** i
    return answer


for i in range(T):
    N, J = map(int, raw_input().split())
    count = 0
    #non_triv_lst = []
    print "Case #" + str(i+1) + ":"
    for j in range(2 ** (N - 1) + 1, 2 ** N, 2):
        if(count >= J):
            exit()
        non_triv_lst = []
        b_str = format(j, 'b')
        all_notriv = True
        for k in range(2,11):
            divisor = find_divisor(value_in_base(b_str, k))
            if(divisor < 0):
                all_notriv = False
                break;
            non_triv_lst.append(divisor)
        if not all_notriv:
            continue
        print b_str,
        for i in non_triv_lst:
            print i,
        print ""
        count += 1






