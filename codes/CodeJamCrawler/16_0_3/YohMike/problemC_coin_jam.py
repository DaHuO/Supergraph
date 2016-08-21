import os
import sys
import itertools
from math import sqrt
from random import randint,sample
"""
I know there are many jamcoins so i am not wasting my time more than 
MAX_NUMBER for a single jamcoin
"""
MAX_NUMBER = 999999 


def output_format(list_number_divisors,test_case):
    output = "Case #%d:\n" % (test_case+1)
    for number,divisors in list_number_divisors.items():
        output += "%s " % str(number)
        for divisor in divisors:
            output +="%d " % divisor
        output +="\n"
    return output


def interpret_in_base(binary_number,base):
    digits = str(binary_number)
    number = 0
    for i in range(len(digits)):
        number += (base ** i )*int(digits[len(digits)-i-1])
    return number

def nontrivial_first_divisor(number):
    #print "Testing for %d"%number
    for i in itertools.count(2):
        if number % i == 0:
            return i
    	if i >= MAX_NUMBER:
    		return -1

def build_base_jamcoin(length):
    return "1" + "0"*(length-2) + "1"


def test_jamcoin_for_prime(jamcoin,jamcoin_dict):
    divisors = []
    for i in range(2,11):
        j_number = interpret_in_base(jamcoin,i)
        base_div = nontrivial_first_divisor(j_number)
        if base_div != -1:
            divisors.append(base_div)
        else:
            print "Jamcoin %s is prime %d" %(jamcoin,j_number)
            return jamcoin_dict #jamcoin has a prime
    jamcoin_dict[jamcoin] = divisors
    return jamcoin_dict

def generate_jamcoins(length):
    jamcoin = build_base_jamcoin(length)
    how_many_ones = randint(0,length-2)
    positions = sample(range(1,length-1),how_many_ones)
    list_coin = list(jamcoin)
    for i in positions:
    	list_coin[i] = "1"
    return "".join(list_coin)

if __name__ == "__main__":
    #f = open("C-large.in",'r')
    f = open("C-large.in",'r')
    test_cases = int(f.readline())
    out = open("results_C_large.txt",'w')
    #for i in range(2,11):
    #    print interpret_in_base('1001',i)

    print test_cases
    for i in range(test_cases):
        jamcoin_dict = {}
        sting  = f.readline()
        print sting.split(" ")
        N,J = tuple(sting.strip("\n").split(" "))
        print N,J
        #jamcoin = build_base_jamcoin(int(N))
        #print jamcoin
        index = 0
        while(len(jamcoin_dict.keys()) < int(J)):
            j_coin = generate_jamcoins(int(N))
            if j_coin  not in jamcoin_dict.keys():
            	init_len = len(jamcoin_dict.keys())
            	jamcoin_dict = test_jamcoin_for_prime(j_coin,jamcoin_dict)
                after_len = len(jamcoin_dict.keys())
                if after_len > init_len:
                    print "Added jamcoin #%s" %index
                    index +=1
            	
        #test format
        #jamcoin_dict = {"100011":[5, 13, 143, 31,43, 1121, 73, 77, 629]}
        output = output_format(jamcoin_dict,i)
        out.write(output)

