'''
Created on 27 Feb 2016

@author: Josh
'''
import math
import decimal
from itertools import count

def read_input(inputfile):
    i = open(inputfile)
    i = i.readlines()
    N, J = i[1].split()
    print([N, J])
    return [N, J]  

def solve_case(N, J):
    answer = ''
    examples = 0
    for x in range(2 ** (N-2)):      
            coin = bin(x + 2 ** (N-2))[2:] + '1'
            divisors = []
            print(coin)
            for x in range(2,11):
                y = int(coin, x)
                z = 2
                while z <= min([math.sqrt(y), 100]):
                    if y % z == 0:
                        divisors.append(z)
                        break
                    else:
                        z = z+1
            if len(divisors) == 9:
                examples = examples + 1
                answer = answer + str(coin) 
                for i in range(9):
                    answer = answer + ' ' + str(divisors[i])
                answer = answer + '\n'
            print(examples)
            if examples == J:
               break
    print(answer)
    return answer
            
def main(input):
    N, J = read_input(input)
    f = open('C:\\Users\\Josh\\Documents\\Python\\output.txt', 'w')
    string = 'Case #1:\n' + solve_case(int(N), int(J))
    f.write(string)

main('C:\\Users\\Josh\\Documents\\Python\\C-large.in')
#solve_case(6,3)