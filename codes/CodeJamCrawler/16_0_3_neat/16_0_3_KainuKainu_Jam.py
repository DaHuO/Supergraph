# generate base data
T = int(input())
N,J = [int(num) for num in input().split()]
bdict = {}
for i in range(2,11):
    tmp = 1
    bdict[i] = [tmp]
    for j in range(N-1):
        tmp *= i
        bdict[i].append(tmp)

divs = {}
Jlist = []
count = J
for num in range(2**(N-2)):
    s = "{0:b}".format(num).zfill(N-2)[-1::-1]
    sfail = False
    divs[s] = []
    for base in range(2,11):
        val = bdict[base][0] + bdict[base][N-1]
        for i in range(N-2):
            if s[i] == "1":
                val += bdict[base][i+1]
        prime = True
        lim = min(int(val/2)+1,1000000)
        for d in range(2,lim):
            if not (val%d):
                divs[s].append(d)
                prime = False
                break
        if prime:
            sfail = True
            break
    if not sfail:
        Jlist.append(("1"+s+"1")[-1::-1])
        count -= 1
        if not count:
            break

print("Case #1: ")
for num in Jlist:
    print(num,end=" ")
    key = num[N-2:0:-1]
    for i in range(8):
        print(divs[key][i],end=" ")
    print(divs[key][-1])
