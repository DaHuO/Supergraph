import itertools
inputs = input()
tcase = 1
m = 1
def isprime(n):
    n = abs(int(n))
    if n < 2:
        return [0, True]
    if n == 2: 
        return [0, True]    
    if not n & 1: 
        return [0, True]
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return [x, False]
    return [0, True]

#-----------------------------------------------s
tcases = []
while tcase != inputs+1:
    s = str(raw_input())
    tcases.append(map(int, s.split()))
    tcase+=1
#testcases input done
permbin = []
perm = []
for i in tcases:
    print 'Case #'+ str(m)+':'
    permbin = map(list, list(itertools.product("01", repeat=i[0])))
    for j in sorted(permbin):
        x = ''.join(map(str, j))
        if isprime(int(x, 2))[1] == False and x[0] != '0' and x[-1] != '0' and isprime(int(x, 3))[1] == False and isprime(int(x, 4))[1] == False and isprime(int(x, 5))[1] == False and isprime(int(x, 6))[1] == False and isprime(int(x, 7))[1] == False and isprime(int(x, 8))[1] == False and isprime(int(x, 9))[1] == False and isprime(int(x, 10))[1] == False:
            print x +' '+ str(isprime(int(x, 2))[0])+' '+ str(isprime(int(x, 3))[0])+' '+ str(isprime(int(x, 4))[0])+' '+ str(isprime(int(x, 5))[0])+' '+ str(isprime(int(x, 6))[0])+' '+ str(isprime(int(x, 7))[0])+' '+ str(isprime(int(x, 8))[0])+' '+ str(isprime(int(x, 9))[0])+' '+ str(isprime(int(x, 10))[0])
            i[1]-=1
        if i[1] == 0:
            break
    m+=1

 

