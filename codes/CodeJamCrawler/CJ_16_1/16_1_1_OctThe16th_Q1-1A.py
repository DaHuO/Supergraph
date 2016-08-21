f = open('A-large.in', 'r')
a = int(f.readline())

for j in range(a):
    b = f.readline().strip("\n")
    b = list(b)
    c = b[0]
    for i in range(1,len(b)):
        if c[0] > b[i]:
            c = c + b[i]
        else:
            c = b[i] + c
    print("Case #" + str(j + 1) + ": " + c)