import math

T = input("Input T: ")

N = [0] * T
print "Input N: "
for i in range(0,T):
    N[i] = input()

Cover = [0] * T
for i in range(0,T):
    if N[i] != 0:
        alphabet = set(str(N[i]))
        Limit = int(pow(10, math.ceil(math.log(N[i], 10)+1)))
        current = N[i]

        while current <= Limit:
            current += N[i]
            alphabet = alphabet | set(str(current))

            if len(alphabet) == 10:
                Cover[i]=current
                break

for i in range(0,T):
    if Cover[i] == 0:
        print "Case #", i+1, ": INSOMNIA"
    else:
        print "Case #", i+1, ":", Cover[i]
