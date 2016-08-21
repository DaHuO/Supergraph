import sys
import time
import numpy as np
from collections import defaultdict

class ProblemSet:
  def __init__(self):
    self.numCases = int(sys.stdin.readline().strip())
  def do_all_cases(self):
    for n in range(self.numCases):
      cp = Problem(n+1)
      cp.do_it()

key = { 1: 'ONE'
      , 2: 'TWO'
      , 3: 'THREE'
      , 4: 'FOUR'
      , 5: 'FIVE'
      , 6: 'SIX'
      , 7: 'SEVEN'
      , 8: 'EIGHT'
      , 9: 'NINE'
      , 0: 'ZERO'
      }
class Problem:
  def __init__(self, caseNum):
    self.case_num = caseNum

  def do_it(self):
    word = sys.stdin.readline().strip()
    kdic = defaultdict(set)
    for dig, stri in key.items():
      for cha in stri:
        kdic[cha].add(dig)
    # for dig, st in kdic.items():
    #   print dig, st
    incnt = defaultdict(int)
    for inch in word:
      incnt[inch] +=1
    
    stuff_left = True
    soln_ct = dict()
    # print incnt
    while incnt:
      for slv_dig, test_char in [(0,'Z'),
                                 (2,'W'),
                                 (4,'U'),
                                 (6,'X'),
                                 (8,'G'),
                                 (3,'T'),
                                 (5,'F'),
                                 (1,'O'),
                                 (7,'S'),
                                 (9,'N')]:
        # print incnt
        # time.sleep(0.1)
        if test_char in incnt:
          soln_ct[slv_dig] = incnt[test_char]/sum([1 if ch==test_char else 0 for ch in key[slv_dig]])
          for rem_cha in key[slv_dig]:
            incnt[rem_cha] -= soln_ct[slv_dig]
            if incnt[rem_cha] == 0:
              del incnt[rem_cha]
          continue
    #print soln_ct
    outstr = ''.join(sum([[str(dig)]*soln_ct[dig] for dig in sorted(soln_ct.keys())], []))

    sys.stdout.write('Case #{}: {}\n'.format(self.case_num, outstr))

def main():
  ProblemSet().do_all_cases()
  

main()
