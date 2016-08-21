import csv


def dec(N):
    s = set([])

    on = True
    while(on):
        nd = N//10
        md = N%10
        s.add(md)
        if nd == 0:
            on = False
        else:
            N = nd
    return s


fileName = "A-large.in";
CSVReader = csv.reader(open(fileName), delimiter=',')
data = list(CSVReader)
data = [int(data[i][0]) for i in range(len(data))]

res = [0 for i in range(len(data)-1)]

for i in range(1,len(data)):
    print("i: " + str(i))
    mainN = data[i]
    #print("N: " + str(mainN))
    s10 = set([])
    for j in range(1,10000000):
        N = mainN*j
        #print("j: " + str(j) + " N: " + str(N))
        s = dec(N)
        s10 = s10 | s
        #print(s10)

        if len(s10) == 10:
            res[i-1] = N
            #print(N)
            break;
    if len(s10) < 10:
        res[i-1] = "INSOMNIA"

f = open("resultLarge.dat","w")

for i in range(len(res)):
    s = "Case #" + str(i+1) + ": " + str(res[i]) + "\n"
    f.write(s)
    print(s)

f.close()






