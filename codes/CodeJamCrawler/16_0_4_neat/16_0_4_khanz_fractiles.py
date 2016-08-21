def check(K, C, S):
    if (C==1 and K>S) or (K > 2*S):
        return "IMPOSSIBLE"
    result = ''
    if (C == 1):
        for i in range(1, K+1):
            result += ' '+str(i)
    else:
        last = 0
        cleared = 0
        step = K**(C-1)
        stepp = K**(C-2)
        while cleared < K:
            result += ' '+str(min(last+(cleared+2)*stepp, K**C))
            last += 2*step
            cleared += 2
    return result[1:]

def main():
    n = int(input())
    K = []
    C = []
    S = []
    for i in range(n):
        line = input().split(' ')
        K.append(int(line[0]))
        C.append(int(line[1]))
        S.append(int(line[2]))
    for i in range(n):
        print('Case #{}: {}'.format(i+1, check(K[i], C[i], S[i])))


if __name__ == "__main__":
    main()
