tc = int(input())
i1 = 0
for i in range(tc):
    i1 += 1
    n = int(input())
    n1 = n
    dig = set()
    l = len(dig)
    count = 2
    while True:
        if(n == 0):
            print("Case #"+str(i1)+": INSOMNIA")
            break
        else:
            l1 = l
            for char in str(n):
                dig.add(int(char))
            if(len(dig) == 10):
                print("Case #"+str(i1)+": "+str(n))
                break
            else:
                n = n1 * count
                count += 1
            
