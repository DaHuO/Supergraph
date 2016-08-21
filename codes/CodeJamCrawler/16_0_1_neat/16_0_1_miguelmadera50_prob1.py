def solution(n):
    q = long(n)
    if n == '0':
        return "INSOMNIA"
    arr = map(str, range(10))
    i = 1

    while True:
        n = long(q * i)
        for digit in str(n):
            if digit in arr:
                arr.remove(digit)
        i += 1
        if len(arr) is 0:
            return n

t = int(raw_input())
for i in range(1, t + 1):
    num = raw_input()
    print "Case #{0}: {1}".format(i, solution(num))