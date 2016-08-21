import math
import numpy

def findjams(jlis,j):
    d={}
    jams=0
    
    prime=isprime()
    for i in jlis:
        if jams==j:
            
            return d
        else:
            t=decnos(i)
            tnt=[]
            for k in t:
                if (k in prime):
                    break
            
                else:
                    tnt.append(subdivisors(k))
            if (k in prime):
                continue
            d[i]=t,tnt
            jams=jams+1
            print jams,d[i]
    return d

def prime6(upto):
    primes=numpy.arange(3,upto+1,2)
    isprime=numpy.ones((upto-1)/2,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2:(upto-1)/2:factor]=0
    return numpy.insert(primes[isprime],0,2)

def isprime():
    n=2**16
    l=prime6(n)
    return l

def decnos(i):
    l=[]
    leng=len(i)
    two,three,four,five,six,seven,eight,nine,ten=0,0,0,0,0,0,0,0,0
    for bit in range(leng):
        two=two+int(i[bit])*(2**bit)
        three=three+int(i[bit])*(3**bit)
        four=four+int(i[bit])*(4**bit)
        five=five+int(i[bit])*(5**bit)
        six=six+int(i[bit])*(6**bit)
        seven=seven+int(i[bit])*(7**bit)
        eight=eight+int(i[bit])*(8**bit)
        nine=nine+int(i[bit])*(9**bit)
        ten=ten+int(i[bit])*(10**bit)

    l=[two,three,four,five,six,seven,eight,nine,ten]
    return l

def subdivisors(k):
    for i in range(2,k):
        if k%i==0:
            return i
        



def generatejam(n):
    l=[]
    for i in range(2**(n-2)):
        s=[]
        t=bin(i)
        s='1'+t[2:].zfill(n-2)+'1'
        l.append(s)
    return l


###################################################################

t=int(raw_input())
for test in range(t):
    n,j=map(int,raw_input().split())

    # n: length of jamcoin
    # j: no of jamcoins

    jlis=[]

    #generate all possible coins of length n

    jlis=generatejam(n)
    


    #find jams
    r=findjams(jlis,j)
    for key,value in r.items():
        print key,' '.join(map(str,value[1]))
