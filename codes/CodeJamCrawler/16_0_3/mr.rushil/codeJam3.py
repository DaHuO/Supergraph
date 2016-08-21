import math
import time
import itertools
import sys

def bin_to_base_n(bin, n):
    value = 0;
    bin = bin[::-1]
    for place in range(0, len(bin)):
        value += int(bin[place]) * n**place
    return value

def get_triv_fact(num):
    if num % 2 == 0 and num > 2:
        return 2
    
    for fact in range(3, int(math.sqrt(num)) + 1, 2):
        if num % fact == 0:
            return fact
    return -1

def is_prime_num2(num):
    if num % 2 == 0 and num > 2:
        return False
    return all(num % fact for fact in range(3, int(math.sqrt(num)) + 1, 2))

def get_coins(length):
    for x in itertools.product('01', repeat=length-2):
        yield '1' + ''.join(x) +'1'

def is_jam_coin(coin):
    return coin[0] == '1' and coin[-1] == '1'



input_data = sys.stdin.readlines()
start_time = time.time()

num_cases = int(input_data[0].replace("\n",""))
for case in range(1, num_cases + 1):
    print "Case #"+str(case)+":"
    values = input_data[case].split(" ")
    n = int(values[0])
    j = int(values[1])

    jams_found = 0
    coins = get_coins(n)
    evidence = ""
    while jams_found != j:
        coin = coins.next()
        while(not is_jam_coin(coin)):
            coin = coins.next()
        evidence = ""
        for base in range(2,11):
            base_n = bin_to_base_n(coin, base)
            triv_fact = get_triv_fact(base_n)
            if triv_fact == -1:
                break
            else:
                evidence = evidence + str(triv_fact) +" "
        else:
            jams_found = jams_found + 1
            print coin, evidence
