def swap(d):
    return [1-i for i in d][::-1]


def verify(d):
    for i in d:
        if i==0:
            return False
    return True


def solve(d):
    moves = 0
    while(not verify(d)):
        moves += 1

        lastzero = len(d)-1
        while d[lastzero]!=0:
            lastzero-=1

        if d[0]==0 and d[lastzero]==0:
            if lastzero == len(d)-1:
                d = swap(d)
            else:
                d = swap(d[:lastzero+1]) + d[lastzero+1:]

        else:
            prev = 0
            maxn = 0
            maxi = 0

            for index, i in enumerate(d[:lastzero]):
                if i == 1:
                    prev+=1
                    if prev>maxn:
                        maxn = prev
                        maxi = index
                else:
                    prev = 0

            d = swap(d[:maxi+1])+d[maxi+1:]

    return moves

def convert(c):
    if c == '+':
        return 1
    else:
        return 0

cases = int(input())
d = []

for i in range(cases):
    a = str(input())
    d.append([convert(c) for c in a])

for index, i in enumerate(d):
    print("Case #{}: {}".format(index+1, solve(i)))



