# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:39:32 2016

@author: chenchen
"""

#use heapq
#from heapq import *

from collections import Counter
#use math 

#test stdin
class Solution():
    def __init__(self, in_string = ""):
        self._s = in_string
        self._counter = Counter(self._s)
        self._number = Counter()
        
        
    def get_nums(self):
        #for 0: z:
        self._number[0] = self._counter["Z"]
        self._counter["Z"] -=  self._number[0]
        self._counter["E"] -=  self._number[0]
        self._counter["R"] -=  self._number[0]
        self._counter["O"] -=  self._number[0]
        
        #for six: x
        self._number[6] = self._counter["X"]
        self._counter["S"] -=  self._number[6]
        self._counter["I"] -=  self._number[6]
        self._counter["X"] -=  self._number[6]
        
        #for 2: w
        self._number[2] = self._counter["W"]
        self._counter["T"] -=  self._number[2]
        self._counter["W"] -=  self._number[2]
        self._counter["O"] -=  self._number[2]        
        
        #for 4: u
        self._number[4] = self._counter["U"]
        self._counter["F"] -=  self._number[4]
        self._counter["O"] -=  self._number[4]
        self._counter["U"] -=  self._number[4]
        self._counter["R"] -=  self._number[4]
        
        #for 8: g
        self._number[8] = self._counter["G"]
        self._counter["E"] -=  self._number[8]
        self._counter["I"] -=  self._number[8]
        self._counter["G"] -=  self._number[8]
        self._counter["H"] -=  self._number[8]
        self._counter["T"] -=  self._number[8]
        
        #for 3: H
        self._number[3] = self._counter["H"]
        self._counter["T"] -=  self._number[3]
        self._counter["H"] -=  self._number[3]
        self._counter["R"] -=  self._number[3]
        self._counter["E"] -=  self._number[3]
        self._counter["E"] -=  self._number[3]
        
        #for 7: S
        self._number[7] = self._counter["S"]
        self._counter["S"] -=  self._number[7]
        self._counter["E"] -=  self._number[7]
        self._counter["V"] -=  self._number[7]
        self._counter["E"] -=  self._number[7]
        self._counter["N"] -=  self._number[7]
        
        #for 5: F
        self._number[5] = self._counter["F"]
        self._counter["F"] -=  self._number[5]
        self._counter["I"] -=  self._number[5]
        self._counter["V"] -=  self._number[5]
        self._counter["E"] -=  self._number[5]
        
        #for 1: O
        self._number[1] = self._counter["O"]
        self._counter["O"] -=  self._number[1]
        self._counter["N"] -=  self._number[1]
        self._counter["E"] -=  self._number[1]
        
        #for 9: I
        self._number[9] = self._counter["I"]
        self._counter["N"] -=  self._number[9]
        self._counter["I"] -=  self._number[9]
        self._counter["N"] -=  self._number[9]
        self._counter["E"] -=  self._number[9]
        
    #use in sort function etc
    def result(self):
        self.get_nums()
        l = list(self._number.elements())
        l_return = map(str,l)
        return "".join(l_return)
        
    def compare_key(self):
        return self._s
        
    #to print the reult
    def to_print(self):
        return str(self._counter)
        
    #s
    def __repr__(self):
        return "solution class to the problem"
    
    #print s    
    def __str__(self):
        return self.to_print()


#w = open(w_name, 'w')

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        
        #readin the input
        input_string = raw_input()
        
        #initilize the soluton
        s = Solution(in_string = input_string)
        
        #output the solution
        print "Case #"+str(case + 1)+":", s.result()
    #    alien_number, source_language, target_language \
    #    = raw_input().split()
    #   K, C, S = raw_input().split()
    #    
    #    base = len(source_language)
    #    temp_result = 0
    #    #print source_language
    #    for s in alien_number:
    #        #print temp_result , s , base, source_language.index(s)
    #        temp_result = source_language.index(s) + temp_result * base
    #        #print temp_result
    #    #translate into target language:
    #    result = ""
    #    base_target = len(target_language)
    #    #print temp_result
    #    while(temp_result != 0):
    #        remainder = temp_result % base_target
    #        result = target_language[remainder] + result
    #        temp_result /= base_target
    #    print("Case #" + str(case+1) +": "+result + "\n")
        
if __name__ == "__main__":
    main()