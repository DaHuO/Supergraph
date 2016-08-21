T = int(raw_input())

init = [False]*10

def check(v):
    return all(v)

def set_digits(v, s):
    for char in s:
        v[int(char)] = True

for i in xrange(T):
    N = int(raw_input())

    answer = None
    if N == 0:
        answer = "INSOMNIA"
    else:
        digits = init[:]
        answer = N
        set_digits(digits, str(answer))

        while True:
            answer += N
            set_digits(digits, str(answer))
            if check(digits):
                break

    print "Case #" + str(i+1) + ":", answer



