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
    nint = int(self.istrm.readline())
    to_get = set([ch for ch in '1234567890'])
    chkl = 1
    while chkl < nint*10:
      chkl *= 10
    chk = 0
    while (chk < chkl) and (to_get):
      chk += 1
      chkn = nint*chk
      chknl = [ch for ch in str(chkn)]
      to_get -= set(chknl)
    if to_get:
      self.ostrm.write('Case #{}: {}\n'.format(caseNum, 'INSOMNIA'))
    else:
      self.ostrm.write('Case #{}: {}\n'.format(caseNum, chkn))

def main():
  dut = Problem(sys.stdin, sys.stdout)
  dut.do_all_cases()

if __name__ == '__main__':
  main()
