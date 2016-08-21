def trot(n):
    seen = {}
    i = 1
    tmp = n
    
    if n == 0:
        return "INSOMNIA"

    while True:
        while tmp >= 1:
            seen[tmp%10] = 1
            tmp = tmp // 10
        if len(seen) == 10:
            return str(n*(i-1))
        else:
            tmp = n*i
            i+=1


f = open('A-large.in.txt', 'r')
num = f.readline()
num = int(num)
c = 1
for line in f:
    print("Case #" + str(c) + ": " + trot(int(line)))
    c+=1