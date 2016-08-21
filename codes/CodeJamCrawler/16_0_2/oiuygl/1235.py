test = int(input())
for i in range(test):
    a = input()
    k = a[0]
    g = 0
    z = 0
    for i in range(-len(a), -1,-1):
        if i != "+":
            break
        z+=1
    for j in range(1, len(a)-z):
        if k != a[j]:
            k = a[j]
            g+=1
    if a[len(a)-1] == "-":
        g+=1
    print("Case #"+str(i+1)+": "+str(g))
            
    
