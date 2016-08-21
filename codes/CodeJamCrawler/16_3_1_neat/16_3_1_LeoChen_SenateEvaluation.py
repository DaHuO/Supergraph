# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:39:32 2016

@author: chenchen
"""

#use heapq
from heapq import *

#use math 

#test stdin
class Solution():
    def __init__(self,p = 0, pi = []):
        self._currentMembers = 0
        
        #a dic
        self._partyMembers = dict()
        self._p = p
        self._pi = pi
        self.partyMap()
        
    def partyMap(self):
        party = "A"
        for i in xrange(self._p):
            self._partyMembers[party] = self._pi[i]
            party = chr(ord(party) + 1)
            self._currentMembers += self._pi[i]
        #test:
        #print self._partyMembers
        
    #use in sort function as a generator
    def generateAnswer(self):
        if self._currentMembers == 0:
            print "empty"
        sortedDict = sorted(self._partyMembers, key = self._partyMembers.get, \
        reverse = True)
            
        s0 = sortedDict[0]
        s1 = sortedDict[1]
        ##even :
        if self._currentMembers % 2 == 0:
            self._partyMembers[s0] -= 1
            self._partyMembers[s1] -= 1
            self._currentMembers -= 2
            return sortedDict[0]+sortedDict[1]
        else:
            self._partyMembers[s0] -= 1
            self._currentMembers -= 1
            return sortedDict[0]
    
    def compare_key(self):
        return self._x
        
    #to print the reult
    def to_print(self):
        while self._currentMembers > 0:
            print self.generateAnswer(),
        #return str(self._p)
        
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
        
        #readin the party numbers
        p = int(raw_input())
        
        #initilize the soluton
        pi = map(int, raw_input().split())
        
        s = Solution(p, pi)
        
        
        
        
        #output the solution
        print "Case #"+str(case + 1)+":", #s 
        s.to_print()
        print
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