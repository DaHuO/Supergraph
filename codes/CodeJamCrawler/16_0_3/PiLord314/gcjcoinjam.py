from math import pow
def dTob(n):
    amp = 1
    total = 0
    while n>0:
        total+=(n%2)*amp
        n=int(n//2)
        amp*=10
    return total
        
        
def coin(n,b):
    amp = 1
    num = n
    total = 0
    while num > 0:
        total += amp*(num%10)
        num = int(num//10)
        amp *= b
    return total

def isPrime(n):
    #Checks if a number is prime
    #returns the greatest nontrivial factor of a number
    #or 1 if prime
    i = 2
    while i*i <= n:
        if(n%i == 0):
            return i
        i= i+1
    return 1

def coinTest(n,primes):
    #output
    ans = [0]*10
    ans[0] = n
    for i in range(2,11):
        #number to check
        check = coin(n,i)
        #Debugging
        #print(check)
        #check if number has not been checked
        #if primes[check] == 0:
            #primes[check] = isPrime(coin(n,i))
        #if primes[check] == 1:
            #return []
        temp = isPrime(coin(n,i))
        if(temp == 1):
            return []
        ans[i-1] = temp

    return ans


def test2():
    primes = [0]*1000000
    ans = coinTest(101001,primes)
    return ans

def test3():
    size = 6
    for i in range(0,int(pow(2,size - 2))):
        case = int(pow(10,size - 1)) + (dTob(i))*10 + 1
        print(case)

def main():
    size = 16
    Cases = [[0]]*50
    casei = 0
    primes = []
    #for i in range(0,pow(10,size))
   #     primes = primes + primes[]
        
    #primes = [0]*int(pow(10,size)+1)
    for i in range(0,int(pow(2,size-2))):
        case = int(pow(10,size-1)) + (dTob(i))*10 + 1
        ans = coinTest(case,primes)
        #Debugging
        #print(ans, len(ans))
        if(len(ans) == 10):
            Cases[casei] = ans
            casei += 1
            print(case)
        if(casei == len(Cases)):
            print("Case #1:")
            for case in Cases:
                temp = ''
                for num in case:
                    temp += str(num) + " "
                print(temp)
            return
