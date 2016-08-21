"""
problema 1
Counting sheep
"""


def dameRes(casoActual):
    N = casoActual[0]
    digits = []
    i = 0
    while i <= 1500:
        i += 1
        counter = i*N
        for n in str(counter):
            n = int(n)
            if n not in digits:
                digits.append(n)
                if len(digits) == 10:
                    return counter

    return "INSOMNIA"




t = int(raw_input())
for ti in range(1, t+1):
    casoActual = [s for s in raw_input().split(" ")]
    casoActual[0] = int(casoActual[0])
    print "Case #{}: {}".format(ti, dameRes(casoActual))