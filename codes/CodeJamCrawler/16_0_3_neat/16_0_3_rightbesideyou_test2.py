import math

a=[1,2,3,4,5,6,7,8,9]

def isPrime(n):
    if n <= 1:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return i
    return 0

fp_in = open('C-small-attempt0.in', 'r+')
fp_out = open('out.txt', 'w+')
T = fp_in.readline()
T = int(T)
for x in range(1, T+1, 1):
    fp_out.write('Case #%d:\r' %(x))
    w = fp_in.readline()
    w = w.split('\n')[0]
    N=w.split('\n')[0].split(' ')[0]
    J=w.split('\n')[0].split(' ')[1]
    #print(N)
    #print(J)
    start='1'+(int(N)-2)*'0'+'1'
    end='1'+(int(N)-2)*'1'+'1'

    count=0
    for i in range(int(start,2),int(end,2)+1,2):
        num=bin(i)
        #print(num)
        for base in range(2,11):
            n10=int(str(num).split('0b')[1],base)
            a[base-2]=isPrime(n10)
            if a[base-2] == 0:
                break
            if base==10:
                #print(str(num).split('0b')[1])
                print(str(num).split('0b')[1] + ' %d %d %d %d %d %d %d %d %d '%( a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8] ))
                fp_out.write(str(num).split('0b')[1] + ' %d %d %d %d %d %d %d %d %d\r'%( a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8] ))
                count=count+1
        if count==int(J):
            break



#    fp_out.write('Case #%d: %d\r' %(x, m1))

fp_in.close()
fp_out.close()