import random
def checkPrime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
def findDivisor(n):
    for i in xrange(2,n/2+1):
        if n%i==0:
            return i
def createcoins(N,J,coins):
    c=0
    while c<J:
         jam=''
         jam+=str(1)
         for i in range(N-2):
             if random.randint(2,100)%2==0:
                 jam+=str(0)
             else:
                 jam+=str(1)
         jam+=str(1)         
         temp=[]
         temp=[int(jam,base) for base in xrange(2,11)]
         #check if any interpretation is prime
         flag=False
         for i in temp:
             if checkPrime(i):
                 flag=True  # means it is a prime no
                 break
         if not flag and jam not in coins:
             coins[jam]=temp             
             c=c+1
def main():
    T=int(raw_input())
    counter=0
    while counter<T:
        N=int(raw_input())
        J=int(raw_input())
        coins={}
        createcoins(N,J,coins)
        #print coins
        print 'Case #%d:'%(counter+1)
        for i in coins:
            print '%s'%(i),
            for j in coins[i]:
                tp=findDivisor(j)
                print '%d'%(tp),
            print ''
        counter=counter+1
if __name__=='__main__':
    main()



    
        
