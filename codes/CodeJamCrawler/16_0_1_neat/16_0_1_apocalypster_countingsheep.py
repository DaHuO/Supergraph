def sheep(n):
    if n == '0':
        return "INSOMNIA"
    notyet = [0,1,2,3,4,5,6,7,8,9]
    copy = n
    while len(notyet)>0:
        for c in copy:
            if int(c) in notyet:
                notyet.remove(int(c))
        copy = str(int(copy) + int(n))

    return str(int(copy)-int(n))

    
        

f = open("sheep.in",'r')
T = int(f.readline().strip())
for i in range(1,T+1):
    print "Case #" + str(i) + ": " + sheep(f.readline().strip())

f.close()
