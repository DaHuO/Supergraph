t = int(input())

output = open("output.txt", "w")

for i in range(1, t +1):
    n = int(input())
    
    senators = input()
    senators = senators.split(" ")
    for j in range(n):
        senators[j] = int(senators[j])

    plan = ""
    
    while senators.count(0) != n:
        e1 = -1
        e2 = -1

        for a in range(n):
            if senators[a] > e1:
                e1 = senators[a]
        e1 = senators.index(e1)
        senators[e1] = senators[e1]-1

        for b in range(n):
            if senators.count(1) == 2 and senators.count(0) == n-2:
                break
            
            else:
                if senators[b] > e2:
                    e2 = senators[b]
        if e2 != -1:
            e2 = senators.index(e2)
            senators[e2] = senators[e2]-1
        
        plan = plan + chr(ord(str(e1))+17)
        if e2 != -1:
            plan = plan + chr(ord(str(e2))+17) + " "
        else:
            plan = plan + " "

    
    output.write("Case #{}: {}\n".format(i, plan))
    print("Case #{}: {}\n".format(i, plan))
    
output.close()
