__author__ = 'igor'


T = int(input())
sol = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
for i in range(T):
    n = int(input())
    j = 0
    s = set()
    while True:
        j +=1
        num = set(list(str(j*n)))
        s = s.union(num)

        if not sol.difference(s):
            print("Case #"+str(i+1)+": "+str(j*n))
            break;
        elif j == 100 and len(s) <= 1:
            print("Case #"+str(i+1)+": INSOMNIA")
            break;




