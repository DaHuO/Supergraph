numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
def canFind(digit, S):
    for letter in numbers[digit]:
        if letter not in S:
            return False
        else:
            S.remove(letter)
    return True

def ren(S, digit):
    for letter in numbers[digit]:
        S.remove(letter)
    return S

def findnumbers( S, d, sf ):
    if len(S) > 0 and d< 10:
        for digit in range(d, 10):
            tmpS = S[:]
            while canFind(digit, tmpS[:]):
                remS = ren(tmpS, digit)
                r= findnumbers(remS, digit, sf + ( digit, ))
                if len(r) > 0:
                    return r
        return tuple()
    elif len(S) == 0:
        return sf
    else: 
        return tuple()


def sol(s):
    return "".join(map(str, findnumbers( list(s), 0, tuple())))

x = int(raw_input())
for i in xrange(1, x+ 1):
    s = raw_input()
    solution = sol(s)
    print "Case #{}: {}".format( i, solution)
