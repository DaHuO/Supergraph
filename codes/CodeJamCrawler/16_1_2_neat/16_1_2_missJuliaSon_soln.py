import sys
from collections import defaultdict

class ProblemSet:
  def __init__(self):
    self.numCases = int(sys.stdin.readline().strip())
  def do_all_cases(self):
    for n in range(self.numCases):
      cp = Problem(n+1)
      cp.do_it()

class Problem:
  def __init__(self, caseNum):
    self.case_num = caseNum

  def do_it(self):
    N = int(sys.stdin.readline().strip())
    ht_par = defaultdict(bool)
    for n in range(2*N-1):
      for f in sys.stdin.readline().strip().split():
        ht_par[int(f)] ^= True
    #print ht_par
    out = sorted([k for k,v in ht_par.items() if v])
    sys.stdout.write('Case #{}: {}\n'.format(self.case_num, ' '.join([str(f) for f in out])))

def main():
  ProblemSet().do_all_cases()
  

main()
