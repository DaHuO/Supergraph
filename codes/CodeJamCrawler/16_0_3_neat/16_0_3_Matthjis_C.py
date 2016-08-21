import sys
import numpy as np

def check_prime(n):
    if n % 2 == 0:
        return 2
    i = 3
    while i <= n**0.5+1:
        if n % i == 0:
            return i
        i+=2
    return 0
    
def bases(N, n, amount, J, answer):
    base = np.zeros((9,N))
    for i in range(0,9):
        for j in range(N):
            base[i,N-j-1] = (i+2)**j
    
    numbers = n*base
    interpretation = np.sum(numbers, axis = 1 )
    factor = np.zeros(9)    
    for i in range(len(interpretation)):
        j = 1
        factor[i] = check_prime(interpretation[i]) #when 0, it's prime, otherwise its a nontrivial factor
        
    if not 0 in factor:
        amount += 1
        jam_coin = ''
        factors = ''
        for digit in n:
            jam_coin += str(int(digit))
        for digit in factor:
            factors += str(int(digit))
            factors += ' '
        print >>answer, "{0} {1}".format( jam_coin, factors)
        if amount == J:
            return None  
    return amount
    
def make_numbers(N, J, answer):
    number = np.zeros(N)
    number[0] = 1
    number[N-1] = 1
    amount = 0 
    
    for i in range(1,N-2):
        n = np.copy(number)
        n[i] = 1
        for j in range(i, N-1):
            n[j] = 1
            amount = bases(N,n, amount, J, answer)
            if amount == None:
                return 
          
def cases(): 
    answer = open('C-small_answer.in', 'w')
    print >>answer, 'Case #1: '
    T = int(raw_input())
    N,J = [int(s) for s in raw_input().split(" ")]
    make_numbers(N,J, answer)
    answer.close()
    
def main():
    cases()
    
if __name__ == '__main__':
    sys.exit(main())