import math
all_primes = []

def andi(a):
    global all_primes
    if a in all_primes:
        return true

    n = a
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    if f not in all_primes :
        all_primes.append(f)
    return True  
    
def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step
        
def is_prime(a):
    global all_primes
    return all(a % i for i in all_primes)
    #return all(a % i for i in xrange(2, int(math.sqrt(a))))
    #return andi(a)
    
def primes(n):
    """ Returns  a list of primes < n """
    n = int(n)
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1):
    #for i in xrange(int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
    
def find_divisor(num) :
    i = 2
    while i < num/2:
        if num % i == 0 :
            return i
        i = i + 1
    return -1
    
def test(num, length) :
    global all_primes
    all_primes = primes(math.sqrt(2**32))
    works = True
    divisors = [-1]*9
    #turn num into int
    x = int(''.join(map(str,num)))
    true_values = []
    for i in xrange(2, 10+1):
        true_x = int(str(x), i) # in base 10
        true_values.append(true_x)
    for item in true_values:
        #print "here"
        if is_prime(item):
            works = False
            return works, divisors
    #print true_values
    base = 2
    while base < 10+1:
        item = true_values[base-2] # base = 2 gets element[0]
        div = find_divisor(item)
        if div == -1:
            works = False
            divisors[base-2] = div
            break
        divisors[base-2] = div
        base = base + 1
    #print true_values
    
    
    return works, divisors
    
def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    #l, d, n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #print l,d,n
    for j in xrange(1, t+1):
        n, j = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in
        my_array = [0]*n
        my_array[0] = 1
        my_array[-1] = 1
        care_about = 2**(n - 2)
        found = 0
        #print n, j, my_array, care_about          
        counter = 0  
        
        j = j
        print "Case #{}:".format(t) 
        while found != j :
            counter = 0
            while counter < care_about:
                b = "{0:b}".format(counter).zfill(n-2)
                binary = [int(e) for e in list(b)]
                binary.insert(0,1)
                binary.append(1)
                works, divisors = test(binary, j)
                if not works:
                    counter = counter + 1
                    #print binary
                    continue
                else :
                    found = found + 1
                    #print binary, works, str(divisors)
                    answer = str(''.join(map(str,binary)))
                    s = ' '.join(map(str,divisors))
                    print answer, s
                    
                    counter = counter + 1
                    if found == j:
                        break
                


            
            
            
        

if __name__ == "__main__" :
    main()
