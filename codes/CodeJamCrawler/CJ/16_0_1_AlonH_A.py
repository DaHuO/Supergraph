f = open("A-large (1).in","r")
o = open("A-large-answers.txt","w")
T = int(f.readline())

for t in range(1,T+1):
    #print("Case "+str(t))
    n = f.readline()
    #if n[-1] == "\n":
    #    n = n[:-1]
    n = int(n)
    #print(n)
    if n == 0:
        o.write("Case #"+str(t)+": INSOMNIA\n")
        continue
    m = n
    n = 0
    s = 1
    l = [1,2,3,4,5,6,7,8,9,0]
    while l:
        n += m
        n1 = n
        while n1:
            try:
                l.remove(n1%10)
            except ValueError:
                pass
            n1 = n1//10
        
    o.write("Case #"+str(t)+": "+str(n)+"\n")
o.close()
"""
f = open("A-test.txt","w")
f.write(str(1001)+"\n")
for i in range(99000,100001):
    f.write(str(i)+"\n")
f.close()"""

