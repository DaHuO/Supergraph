import math
import random
def isprime(inputnum,bs):
    endnum=math.sqrt(inputnum)
    endint=int(endnum)
    #print endint
    flag=0
    if inputnum %3 ==0:
        return 3,1
    else:
        temp1=(float)(inputnum+1)/6
        temp2=(float)(inputnum-1)/6
        #print temp1,temp2
        if isinstance(temp1,int):
            return -1,0
        elif isinstance(temp2,int):
            return -1,0
        for i in xrange(5,endint+1,2):
            if inputnum % i==0:
                return i,1
        if flag==0:
            return -1,0

list=[]
val=0
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in range(0, t):
    n, j = [int(s) for s in raw_input().split(" ")]
#print n,j
#input collected now need to process
#we will test only the numbers in this range
baseStart=pow(2,n-1)+1
baseEnd=pow(2,n)-1
numbersNeeded=j
print
print "Case #1:"
f = open("output_rand.txt", "a")
f.write("Case #1:"+"\n")
f.close()
#print baseStart,baseEnd
listout=[]
while(True):
    #select i randomly between baseStart and baseEnd
    i=random.randrange(baseStart,baseEnd+1,2)
    if i in listout:
        continue
    #print i
    if numbersNeeded<1:
        break
    list=[]
    #print i
    div,result=isprime(i,2)
    #print div,result
    if result==1:
        binary=bin(i)
        list.append(div)
        #now check for each of the bases from 3 to 10 if its is prime or not
        # if all of them say its not prime then our number is jamcoin
        lenbinary=len(binary)
        binarysliced=binary[2:lenbinary]
        lenbinary=len(binarysliced)
        #print binarysliced
        baseSatisfied=0
        for base in xrange(3,11):
            val=0
            counting = 0
            val=int(binarysliced,base)
            """for rev in range(lenbinary-1,-1,-1):
                if binarysliced[rev] == "1":
                    k=pow(base, counting)
                    #print k
                    val+=k
                #print counting
                counting += 1
            counting-=1"""
            #print val
            #we got the respective base value now need to check if the value if prime or not
            # and continue only if the value is not prime for the given base aswell
            div,result=isprime(val,base)
            if result==1:
                list.append(div)
                baseSatisfied+=1
                #print baseSatisfied
                continue
            else:
                break
        if baseSatisfied==8:
            #we have got a jamcoin print the
            #  value
            f=open("output_rand.txt","a")
            f.write(binarysliced+" ")
            print binarysliced,
            for m in range(0,9):
                f.write(str(list[m])+" ",)

                print list[m],
            print
            listout.append(i)
            f.write("\n")
            f.close()
            numbersNeeded-=1

