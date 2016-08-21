import sys
from copy import copy

class Problem:
  def __init__(self, istrm=sys.stdin, ostrm=sys.stdout):
    self.numCases = int(istrm.readline())
    self.istrm = istrm
    self.ostrm = ostrm

  def do_all_cases(self):
    for caseNum in range(1,1+self.numCases):
      self.do_case(caseNum)

  def do_case(self, caseNum):
    (K, C, S) = [int(x) for x in self.istrm.readline().split()]
    inds = [1+N*K**(C-1) for N in range(K)]
    self.ostrm.write('Case #{}: {}\n'.format(caseNum, ' '.join([str(ind) for ind in inds])))

def main():
  dut = Problem(sys.stdin, sys.stdout)
  dut.do_all_cases()

if __name__ == '__main__':
  main()
