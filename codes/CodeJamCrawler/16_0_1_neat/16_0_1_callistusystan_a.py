def intput():
    return int(input())
def insplit():
    return input().split()
def intsplit():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a
def strtolist(a):
    list = []
    for c in a:
        list.append(c)
    return list
def s(a):
    return str(a)

T = intput()
for t in range(T):
    N = input()
    b = N
    i=1
    y=0
    a=[False]*10
    if b=="0":
        b = "INSOMNIA"
    else:
        while True:
            b = str(i*int(N))
            for j in b:
                if a[int(j)] == False:
                    a[int(j)] = True
                    y+=1
                    if y==10:
                        break
            if y==10:
                break
            i+=1

    print("Case #" + str(t+1) + ": " + str(b))
