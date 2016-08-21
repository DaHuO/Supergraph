import itertools,sys,math

def divisor(number):
    for i in range(2,number):
        if number % i == 0:
#            print(i, 'divisor')
            return i

def not_prime(n):
    for i in range(3,n):
        if n % i != 0:
            return True
    return False

def is_primeX(n):
    for i in range(3, n):
        if n % i == 0:
#            print(i, 'prime False')
            return False
        #print(i, 'prime True')
    return True

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def isJamX(number):
    if(number[0] == '1' and number[-1] == '1'):
        arr = []
        for i in range(2,11):
            num = int(number,i)
            if(not_prime(num)):
                arr.append(divisor(num))
            else:
                return(False,[])
        return(True, arr)
        
    return(False,[])

def isJam(number):
    if(number[0] == '1' and number[-1] == '1'):
        arr = []
        for i in range(2,11):
            num = int(number,i)
#            print(i, num, 'isJam')
            #print(num, is_prime(num), divisor(num))
            if(is_prime(num)):
                return (False,[])
            arr.append(divisor(num))
        return (True,arr)
    return (False,[])

def makeJam(N, J):

    num = 0
    arr = list(itertools.product([0,1], repeat = N))
    ret = []
    for i in arr:
        if(num == J): return ret
        temp1 = ''.join(map(str,i))
        temp2 = isJam(temp1)
        if(temp2[0]):
            #print(temp1, ' '.join(map(str,temp2[1])))
            ret.append(temp1 + ' ' + ' '.join(map(str,temp2[1])))
            num += 1
            

if __name__ == "__main__":
    f = sys.stdin
    t = int(f.readline())
    arr = dict()
    for i in range(1,t+1):
        line = f.readline().strip().split()
        arr[i] = makeJam(int(line[0]),int(line[1]))
    for j in arr:
        print("Case #%d:" % (j))
        for k in arr[j]:
            print(k)
