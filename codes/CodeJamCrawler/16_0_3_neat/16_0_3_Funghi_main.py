N = 16
J = 50

s = 129
print("Case #1:")
for i in range(J):
    print((bin(s)[2:])*2, end="")
    for j in range(2, 11):
        print(" {}".format(j**8+1), end="")
    print("")
    s += 2