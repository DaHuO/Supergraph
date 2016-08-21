T = int(raw_input())

def flip(s, n):
    for i in xrange(n):
        s[i] = '+' if s[i] == '-' else '-'

def rev(s, n):
    s[0:n] = s[n-1::-1]

def first_of(s, char):
    for i,c in enumerate(s):
        if c == char:
            return i

    return None

for i in xrange(T):
    S = list(raw_input())
    result = 0
    while True:
        char = '+'
        n = first_of(S, char)

        if n == None:
            result += 1
            break

        if n == 0:
            char = '-'
            n = first_of(S, char)

        if n == None:
            break

        result += 1
        rev(S, n)
        flip(S, n)

    print "Case #" + str(i+1) + ":", result


