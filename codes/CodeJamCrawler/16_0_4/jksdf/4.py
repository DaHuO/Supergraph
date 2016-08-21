def casePrint(n, v):
    print("Case #{}: {}".format(n, v))

def f(number):
    k, c, s = [int(i) for i in input().split()]
    l = k ** c
    step = l // k
    s = ""
    for i in range(0, l, step):
        if i != 0:
            s += " "
        s += str(i+1)
    casePrint(number, s)
        
    

N = int(input())
for n in range(N):
    f(n+1)
