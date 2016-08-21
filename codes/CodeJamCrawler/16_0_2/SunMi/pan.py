a_dict = {'-': '+', '+': '-'}

fd = open("B-large.in")
fd2 = open("B-large.out", "w")

def get_c(a):
    a = list(a)
    l = len(a)-1

    cnt = 0
    while True:
        if a[l] == '-':
            for i in range(l):
                a[i] = a_dict[a[i]]
            cnt += 1
        l -= 1
        if l == -1:
            return cnt

for T in range(int(fd.readline())):
    cat = 1
    for line in fd.readlines():
        fd2.write('Case #' + str(cat) + ': ' + str(get_c(line.strip())) + "\n")
        cat += 1
fd2.close()