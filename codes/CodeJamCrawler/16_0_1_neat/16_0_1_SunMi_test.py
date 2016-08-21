fd = open("A-large.in")
fd2 = open("A-large.out", "w")


def get_sd(start):
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while True:
        i += 1
        start_c = start * i
        for c in str(start_c):
            l[int(c)] = 1
            try:
                l.index(0)
            except:
                return start_c


for T in range(int(fd.readline())):
    cat = 1
    for line in fd.readlines():
        N = int(line)
        if N != 0:
            fd2.write('Case #' + str(cat) + ': ' + str(get_sd(N)) + "\n")
        else:
            fd2.write('Case #' + str(cat) + ': INSOMNIA\n')
        cat += 1
fd2.close()
