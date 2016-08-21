import sys
import numpy as np

def numbercheck(number, asleep):
    while number != 0:
        digit = number % 10
        asleep[digit] = True
        number = (number - digit)/10
    return asleep
    
def counting(c):
    asleep = np.zeros(10)
    i = 0
    number = 0
    while sum(asleep) != 10:   
        i += 1
        number = i * c
        if number > sys.maxint or number == 0:
            return 'INSOMNIA'
        
        numbercheck(number, asleep)
    
    return int(number)

def cases(): 
    answer = open('A-large-answer.in', 'w')
    
    input = np.loadtxt(raw_input(), unpack = True)
    T = int(input[0])
    for i in range(1, T+1):   
        c = input[i]
        print >>answer, "Case #{0}: {1}".format(i, counting(c))
    
    answer.close()
    
def main():
    cases()
    
if __name__ == '__main__':
    sys.exit(main())