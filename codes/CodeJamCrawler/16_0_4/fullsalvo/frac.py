from math import ceil
def solution(K,C,S):
    out = ''
    if (C < 2 and S != K) or (C > 1 and S < K/2.):
        out += 'IMPOSSIBLE'
    elif(C < 2):
        for i in range(1,K+1):
            out += str(i)
            if i != K:
                out += " "
    else:
        if K%2 == 0:
            for i in range(1,(K/2 + 1)):
                out += str(2*(i + (i-1)*K**(C-1)))
                if i != K/2:
                    out += " "
        else:
            lim = int(ceil(K/2.))
            for i in range(1,(lim + 1)):
                if i != lim:
                    out += str(2*(i + (i-1)*K**(C-1))) + " "
                else:
                    out += str(K**C)
    return out

if __name__ == '__main__':
    T = int(raw_input())
    for zz in range(0,T):
        test = str(raw_input()).split()
        K = int(test[0])
        C = int(test[1])
        S = int(test[2])
        print "Case #%s: %s" % (str(zz+1), solution(K,C,S))
