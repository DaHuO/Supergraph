import sys

def isPrime(n, factorsList):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0:
        factorsList.append(2)
        return False
    if n < 9: return True
    if n%3 == 0:
        factorsList.append(3)
        return False
    r = 1000  #taken for ease, otherwise r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0:
            factorsList.append(f)
            return False
        if n%(f+2) == 0:
            factorsList.append(f+2)
            return False
        f +=6
    return True

def stringInterpret(lst, base):
    hPower = len(lst) - 1
    result = 0
    for i in lst:
        result = result + (int(i))*(base**hPower)
        hPower = hPower - 1
    return result

def add(lst_str, a, b, pos):
    if(a == '0'):
        if(b == '0'):
            lst_str[pos] = '0'
            return '0'
        else:
            lst_str[pos] = '1'
            return '0'
    else:
        if(b == '0'):
            lst_str[pos] = '1'
            return '0'
        else:
            lst_str[pos] = '0'
            return '1'
                
def increment(lst_str, N):
    i = -2
    carry = add(lst_str, lst_str[i], '1', -2)
    i = i-1
    while((N > 0) and (carry == '1')):
        carry = add(lst_str, lst_str[i], carry, i)
        i = i-1
        N = N-1

def resultFunction(N, J):
    lst_str = ['1']
    for i in range(N-2):
        lst_str.append('0')
    lst_str.append('1')
  
    while(J > 0):
        factorsList = []
        errorCode = False
        for i in range(2,11):
            ans = stringInterpret(lst_str, i)
            errorCode = isPrime(ans, factorsList)
            if(errorCode == True):
                increment(lst_str, N)
                break
            
        if(errorCode == False):
            print ''.join(lst_str),
            temp = len(factorsList)
            for i in range(temp-1):
                print factorsList[i],
            print factorsList[-1]
            increment(lst_str, N)
            J = J-1
    
def main():
    T = int(raw_input())
    for i in range(T):
        N, J = map(int, raw_input().split())
        print "Case #",; sys.stdout.softspace=False; print (i+1),; sys.stdout.softspace=False; print ":"
        resultFunction(N, J)
        

main()
