fo = open("input.txt", "r")

T = int(fo.readline().strip())
for i in range(T):
    N = int(fo.readline().strip())
    c = 1
    b = set()
    lv = N
    if (N != 0):
        while (not set([str(i) for i in range(10)]) == set(b)):
            lv = c*N
            for char in str(c*N):
                b.add(char)
            c += 1
        print ("Case #" + str(i+1) + ": " + str(lv))
    else:
        print ("Case #" + str(i+1) + ": INSOMNIA")
