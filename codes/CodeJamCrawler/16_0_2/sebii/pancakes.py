from string import maketrans

def flip(S, n):
    t = maketrans('+-', '-+')
    S1 = S[:n].translate(t)
    return S1[::-1] + S[n:]

def solve(S):
    K = [S[i] == S[i + 1] for i in range(len(S) - 1)]
    res = len([k for k in K if not k])

    if S[-1] == '-':
        return res + 1
    else:
        return res

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        S = raw_input()
        print('Case #{}: {}'.format(i + 1, solve(S)))
