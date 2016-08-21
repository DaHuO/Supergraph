def fall(n, k, w):
    sz = 10*[False]
    i = 2
    x = n
    while not all(item == True for item in sz):
        if x == (n * (i - 1) and i != 2):
            break
        if str(x)[0] == '-':
            x = int(str(x)[1:])
        for s in str(x):
            sz[int(s)] = True
        if all(item == True for item in sz):
            break
        else:
            x = i * n
            i += 1

    if all(item == True for item in sz):
        #print("Case #" + str(k) + "): " + str(x))
        w.write("Case #" + str(k) + ": " + str(x) + "")
    else:
        #print("Case #" + str(k) + ': INSOMNIA')
        w.write("Case #" + str(k) + ': INSOMNIA')

f = open("A-large.in", "r")
w = open("A-large.out", "w")
for i in range(0, int(f.readline())):
    fall(int(f.readline()), (i + 1), w)
    if i != 99:
        w.write("\n")

f.close()
w.close()
