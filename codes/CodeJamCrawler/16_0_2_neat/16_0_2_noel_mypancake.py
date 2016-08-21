count = 0

def flip(pks,N):
    global count
    temp = pks[N::-1]
    for i in range(N+1):
        temp[i] = "+" if temp[i] == "-" else "-"
    #print(temp + pks[N+1:])
    count += 1
    return temp + pks[N+1:]



for T in range(int(input())):
    pks = list(input())
    last = len(pks) - 1
    count = 0
    while(pks.count('-') != 0):
        first = -1
        while pks[first + 1] == '+':
            first += 1
        while pks[last] is '+':
            last -= 1
        if(first > -1):
            pks = flip(pks,first)
        pks = flip(pks,last)
    print("Case #" + str(T+1) + ": " + str(count))





