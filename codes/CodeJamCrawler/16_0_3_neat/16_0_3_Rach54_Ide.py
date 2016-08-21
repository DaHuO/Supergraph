# cook your code here
import sys
N = []
listp = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
def Prime(number):
    for j in listp:
        if(number%j==0):
            return 0
    return 1
print "Case #1:"
for i in xrange(32):
    if i==0 or i == 31:
        N.append(1)
    else:
        N.append(0)
k2 = 0
count = 500
nos = [0]*9
while(k2<count):
    flag2=1
    for k in range (2,11):
        number = 0
        for i in xrange(32):
            number = number*k+N[i]
        nos[k-2] = number
        if Prime(number) == 1:
            flag2 = -1
            break
    if(flag2==1):
        k2 += 1
        sys.stdout.write(str(nos[8])+" ")
        for i in xrange(9):
            for j in listp:
                if nos[i]%j==0:
                    sys.stdout.write(str(j)+" ")
                    break
        sys.stdout.write("\n")
    no = nos[0]+2
    l = 0
    while no>0:
        N[31-l] = no%2
        no = (int)((int)(no)/2)
        l = l+1