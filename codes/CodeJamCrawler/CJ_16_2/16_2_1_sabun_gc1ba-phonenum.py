#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sabu
if __name__ == "__main__":
    testcases = int(input())                    #get number of tests
    ntos = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    def decode(sp, dsp):
        ndsp = dsp
        while (sp.count('Z')>0):
            for c in "ZERO":
                sp = sp.replace(c, '', 1)
            ndsp += '0'            
        while (sp.count('X')>0):
            for c in "SIX":
                sp = sp.replace(c, '', 1)
            ndsp += '6'           
        while (sp.count('G')>0):
            for c in "EIGHT":
                sp = sp.replace(c, '', 1)
            ndsp += '8'         
        while (sp.count('U')>0):
            for c in "FOUR":
                sp = sp.replace(c, '', 1)
            ndsp += '4'       
        while (sp.count('F')>0):
            for c in "FIVE":
                sp = sp.replace(c, '', 1)
            ndsp += '5'      
        while (sp.count('V')>0):
            for c in "SEVEN":
                sp = sp.replace(c, '', 1)
            ndsp += '7'   
        while (sp.count('W')>0):
            for c in "TWO":
                sp = sp.replace(c, '', 1)
            ndsp += '2'
        while (sp.count('O')>0):
            for c in "ONE":
                sp = sp.replace(c, '', 1)
            ndsp += '1'
        while (sp.count('H')>0):
            for c in "THREE":
                sp = sp.replace(c, '', 1)
            ndsp += '3'
        while (sp.count('I')>0):
            for c in "NINE":
                sp = sp.replace(c, '', 1)
            ndsp += '9'
        return ndsp
        
    for caseNr in range(1, testcases+1):        #for each testcase
        s = input().strip()
        phone = ''.join(sorted(list(decode(s, ""))))        
        print("Case #%i: %s" % (caseNr, phone))
        