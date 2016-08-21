import math
import itertools

''' Return value of 0 indicates that the number is prime or identity '''
def non_trivial_divisor (number):
    
    if (number < 0):
        raise AssertionError('Number should be positive')
    
    if (number <= 2):
        return 0
    
    answer = 0    
    start = 2
    end = math.ceil(math.sqrt(number))
    
    i = start 
    while (i <= end):
        
        if (number % i == 0):
            answer = i
            return answer
        
        i = i + 1
        
    return answer

def base_n( string, n):

    answer = 0
    if not (string[0] == '1' and string[-1] == '1'):
        raise AssertionError('Not a valid jam coin string')
    
    string = string[::-1]
        
    for i in range(len(string)):
        answer = answer + int(string[i])*(n**i) 
    
    return answer
    
def get_candidates (n):

    if (n < 2):
        raise AssertionError('n should be greater than 2')
        
    candidates = ["".join(seq) for seq in itertools.product("01", repeat=n-2)]
    return [ '1'+cand+'1'  for cand in candidates]
    
def test_base_n (string):

    for i in range(2,11):
        print(base_n(string, i))

def test_non_trivial_divisor(num):

    for i in range(num+1):
        print i, non_trivial_divisor(i)
        
def main():
    
    input_file = 'input.txt'
    f = open(input_file,'r')
    lines = f.readlines()
    T = int(lines[0])
    if not (T == 1):
        print 'T =',T
        raise AssertionError('T should be 1')
        
    tokens = lines[1].split()
    N = int(tokens[0]) 
    J = int(tokens[1])
    print "Case #1:"   
    
    candidates = get_candidates(N)
    count = 0
    
    for cand in candidates:
        divisors = []
        number = 0
        #print cand
        
        for i in range(2,11):
            number = base_n(cand, i)
            div = non_trivial_divisor(number)
            
            #print "Base 10:", number, "Divisor:", div
            
            if (div > 1):
                divisors.append(div)
            else:
                break
        
        if ( len(divisors) == 9):
            print cand,
            for div in divisors:
                print div,
            print 
            count = count + 1
        
        if (count >= J):
            break    
             
#test_base_n('100011')
#test_non_trivial_divisor(20)

main()