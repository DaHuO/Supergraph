fin = open("A-large.in", "r")
fout = open("A-large.out", "w")
T = int(fin.readline())
N = [int(fin.readline()) for e in range(T)]
res = [0 for x in range(10)]
sum = 0

def add(x):
    global sum
    global res
    x = int(x)
    if res[x] < 1:
        res[x] += 1
        sum += 1

for i in range(T):
    sum = 0
    count = 1
    res = list(map(lambda x: 0, res))
    tmp = N[i]
    if N[i] == 0:
        N[i] = "Case #" + str(i + 1) + ": INSOMNIA"
        continue
    while True:
        for j in list(str(tmp)):
            add(j)
        if sum == 10:
            N[i] = "Case #" + str(i + 1) + ": " + str(tmp)
            break
        count += 1
        tmp += N[i]

for i in range(T):
    fout.write(str(N[i]) + "\n")
