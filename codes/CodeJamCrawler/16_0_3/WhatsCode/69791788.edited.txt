import math
def dec_to_bin(x):
    return int(bin(x)[2:])
def solve():
    T = int(raw_input())

    def fromtwotowhat(n, d):
        p = 0
        ans = 0
        while n > 0:
            ans += (n%2)*(d**p)
            p+=1
            n>>=1
        return ans

    def judge(n):
        for i in xrange(2, int(math.sqrt(n))):
            if n % i == 0:
                return i
        return -1

    for i in xrange(T):
        print "Case #1:"
        N, J = map(int, raw_input().split())
        end = 1<<(N-2)
        ans = []
        for j in xrange(end):
            j+=(1<<(N-2))
            j<<=1
            j+=1
            answer = [dec_to_bin(j)]
            for b in xrange(2, 11):
                k = fromtwotowhat(j, b)
                ju = judge(k)
                if ju != -1:
                    answer.append(ju)
                    if len(answer) == 10:
                        ans.append(answer)
                        if len(ans) == J:
                            return ans
                else:
                    break


aa = solve()
for a in aa:
    print ' '.join(map(str,a))