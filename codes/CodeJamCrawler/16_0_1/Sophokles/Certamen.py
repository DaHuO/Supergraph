def multiplier(start):
    coeff = 2
    while True:
        found2 = []
        N = start * coeff
        for finger in digits:
            if finger in str(N):
                found2.append(finger)
        for seen in found2:
            digits.discard(seen)
        if len(digits) == 0:
            return N
            break
        coeff += 1


def printer(first, second):
    print("Case #{}: {}".format(first, second))

def insomnia(first):
    print("Case #{}: INSOMNIA".format(first))


cases = int(input())
for test in range(1,cases+1):
    digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    found1 = []
    num = int(input())
    if num == 0:
        insomnia(test)
    else:
        for finger in digits:
            if finger in str(num):
                found1.append(finger)
        for seen in found1:
            digits.discard(seen)
        if len(digits) == 0:
            printer(num)
        else:
            num = multiplier(num)
            printer(test, num)


