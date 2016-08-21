file1 = open(r"C:\Users\Wu Jui Hsuan\Desktop\abcd.txt","r")
file = open(r"C:\Users\Wu Jui Hsuan\Desktop\gjmi.txt","w")
def mp():  return map(int,input().split())
def lt():  return list(map(int,input().split()))
def pt(x):  print(x)
def ip():  return input()
def it():  return int(input())
def sl(x):  return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x):  return "{0:b}".format(x)
T = int(file1.readline())
for i in range(T):
    n = int(file1.readline())
    if n == 0:
        print("Case #%d: INSOMNIA" % (i+1))
        file.write("Case #%d: INSOMNIA\n" % (i+1))
        continue
    r = set([x for x in str(n)])
    k = n
    while len(r) != 10:
        k += n
        r = r | set([str(x) for x in str(k)])
    print("Case #%d: %d" % (i+1,k))
    file.write("Case #%d: %d\n" % (i+1,k))
        
    
        