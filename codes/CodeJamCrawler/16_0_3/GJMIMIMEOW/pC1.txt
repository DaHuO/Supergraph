def mp():  return map(int,input().split())
def lt():  return list(map(int,input().split()))
def pt(x):  print(x)
def ip():  return input()
def it():  return int(input())
def sl(x):  return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x):  return "{0:b}".format(x)

file1 = open(r"C:\Users\Wu Jui Hsuan\Desktop\csmalll.txt","r")
file = open(r"C:\Users\Wu Jui Hsuan\Desktop\gjmi.txt","w")
def prime(n):
    if n == 2 or n == 3:
        return 0
    if n < 2 or n % 2 == 0:
        return 2
    if n < 9:
        return 0
    if n % 3 == 0:
        return 3
    r = int(n**0.5)
    f = 5
    while f < r:
        if n % f == 0:
            return f
        if n % (f+2) == 0:
            return f+2
        f += 6
    return 0

#T = int(input())
T = int(file1.readline())
for i in range(T):
    print("Case #%d:\n" % (i+1))
    file.write("Case #%d:\n" % (i+1))
    #n,J = mp()
    n,j = map(int,file1.readline().split())
    c = 0
    for m in range(2**((n-2)//2)):
        if c == J:
            break
        s = "{0:b}".format(m)
        s = ''.join([x*2 for x in s])
        s = "1" + "0"*(n-len(s)-2) + s + "1"
        R = [s] + [str(r+1) for r in range(2,11)]
        w = " ".join(R)
        print("%s\n" % w)
        file.write("%s\n" % w)
        c += 1
            

            
            
            
    