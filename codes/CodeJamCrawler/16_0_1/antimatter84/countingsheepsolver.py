#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abstractjamsolver import AbstractJamSolver


class CountingSheepSolver(AbstractJamSolver):
    def solve_case(self):
        digits = "1234567890"
        multi = 1
        number = int(self._infile.readline())
#        print "read number:", number
        
        if number == 0:
            return "INSOMNIA"
        
        history = []
        name = None
        while len(digits)>0:
            name = str(number * multi)
#            print "name=", name
            
            history.append(name)
            if len(history) >= 2 and history[-1] == history[-2]:
                return "INSOMNIA"
                
            for x in name:
                digits = digits.replace(x, "")
#                print "digits=", digits
            multi += 1
        
        return name
                
        
if __name__ == "__main__":
    s = CountingSheepSolver("A-large-sheep-in.txt", "A-large-sheep-out.txt")
    s.solve()