# Fractiles

# LG
# LGGG
# LGGGGGGG

# i = 0
# 2*i + 2 = 2
# 2*2*i + 2*2 + 2 = 6

# i = 1
# 2*1 + 2 = 4
# 2*2*1 + 2*2 + 2 = 10

# 2^2 + 2 = 6
# 

# f(i, l) = L*f(i, l - 1) + K

def print_case(case, res):
    print('Case #%i:' % case, res)

def child(i, C, K):
    if (C <= 1):
        return i;
    return K*child(i, C - 1, K) + K

T = int(input())
for t in range(1, T + 1):
    K,C,S = [int(x) for x in input().split()]
    if(S < K):
        print_case(t, 'IMPOSSIBLE')
        continue
    tiles_to_clean = [child(i, C, K) - child(0, C, K) + 1 for i in range(K)]
    print_case(t, ' '.join(map(str, tiles_to_clean)))
