

import concurrent.futures
import os
import math

def find_div(num):
    if num%2 == 0:
        return 2
    if num%3 == 0:
        return 3
    k=6
    limit = math.ceil(math.sqrt(num))
    while k<=limit:
        if num % (k-1) == 0:
            return k-1
        elif num % (k+1) == 0:
            return k+1
        k+=6
    return -1

def jamcoin_checker(n):
    print(n)
    bin_number = bin(n)[2:]
    if bin_number[-1] == '0':
        return None
    return_list = [int(bin_number)]
    for base in range(2,11):
        new_num = int(bin_number,base)
        divisor = find_div(new_num)
        if divisor != -1:
            return_list.append(divisor)
        else:
            return None
    return return_list
    
        


def main(filename):
    
    with open(filename) as fin:
         data = fin.read().splitlines()
         
    cases = data[0]
    n,j = (list(map(int,data[1].split())))
    min_value = int('1'+'0'*(n-2)+'1',2)
    max_value = int('1' * n,2)+1
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(jamcoin_checker, range(min_value,max_value,2))
        counter = 0
        with open('out.txt','w') as fout:
            fout.write("Case #1:\n")
            for res in results:
                if(res!= None):
                    counter += 1
                    print(counter)
                    fout.write(' '.join(map(str,res))+'\n')
                    if(counter == j):
                        break
        
                
if __name__ == '__main__':
    main('csmall.in')
