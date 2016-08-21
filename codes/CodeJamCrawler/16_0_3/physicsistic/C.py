import sys


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def check_prime(n):
    for p in primes:
        if n % p == 0:
            return p 
    return n

def solve(N,J):
    D = dict()
    for x in range(2,11):
        D[x] = [pow(x,n) for n in range(N)]
    output = '\n'
    counter = 0
    i = 0
    MAX = pow(2,N-2)
    while i < MAX:
        print i
        coins = dict()
        for x in range(2, 11):
            coins[x] = 1 + pow(x,N-1)
        mark = bin(i)[2:].rjust(N-2,'0')
        print mark
        for j in range(len(mark)):
            for k in coins:
                if mark[j] == '1': 
                    coins[k] += pow(k,j+1)
        is_jamcoin = True
        proof_string = str(coins[10])
        for k in coins:
            factor = check_prime(coins[k])
            if factor == coins[k]:
                is_jamcoin = False
                break
            else:
                proof_string += ' ' + str(factor)
        if is_jamcoin:
            output += proof_string + '\n'
            counter += 1
        if counter == J:
            return output
        i+=1






 
def io(filename):
    output = open(filename.split('.')[0]+'.out', 'w')
    with open(filename, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            N, J = map(int,f.readline().rstrip('\n').split())
            string = "Case #{n}: {y}".format(n=t+1, y=solve(N,J))
            print string
            print "======================================================="
            output.writelines(string+'\n')   
 
if __name__ == '__main__':
    input_file = sys.argv[1]
    io(input_file)

