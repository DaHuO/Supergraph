
def run(K, C, S):
    ret = []
    for i in range(K):
        id = i
        for j in range(C - 1):
            id = id * K + id % K
        ret.append(id + 1)
    return ret
            

if __name__ == '__main__':
    for t in range(int(input())):
        result = run(*map(int, input().split()))
        print('Case #{}: {}'.format(t + 1, ' '.join(map(str, result))))
                       
