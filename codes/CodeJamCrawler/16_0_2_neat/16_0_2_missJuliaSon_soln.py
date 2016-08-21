import sys
from copy import copy

class State:
  def __init__(self, ok, n_in=0):
    self.ok = ok
    self.n_in = n_in
    self.flipd = dict()
    # print n_in

  def happy(self):
    return all(self.ok)

  def flip(self, n_to_flip):
    if n_to_flip not in self.flipd:
      new_ok = [not p for p in reversed(self.ok[:n_to_flip]) ] + self.ok[n_to_flip:]
      self.flipd[n_to_flip] = State(new_ok, self.n_in+1)
    return self.flipd[n_to_flip]

  def do_all_flips(self, n_stop):
    # print '{} do all flips {}'.format(self.ok, n_stop, self.n_in)
    if n_stop > self.n_in:
      #max_n = self.ok.index(False)
      for n_to_flip in range(1, len(self.ok)+1):
       #   print 'flipping {}'.format(n_to_flip)
        self.flip(n_to_flip).do_all_flips(n_stop)
      
  def got_a_winner(self):
    # print 'checking for a winner'
    if self.happy():
      # print 'I win {}'.format(self.n_in)
      return self.n_in
    else:
      winner = None
      for succ in self.flipd.values():
        if winner is None:
          winner = succ.got_a_winner()
      return winner
      
class Problem:
  def __init__(self, istrm=sys.stdin, ostrm=sys.stdout):
    self.numCases = int(istrm.readline())
    self.istrm = istrm
    self.ostrm = ostrm

  def do_all_cases(self):
    for caseNum in range(1,1+self.numCases):
      self.do_case(caseNum)

  def do_case(self, caseNum):
    ok = [True if ch=='+' else False for ch in self.istrm.readline().strip()]
    N = len(ok)
    s0 = State(ok)
    ok += [True]
    winner = sum([1 if ok[n] != ok[n+1] else 0 for n in range(0,len(ok)-1)])
    self.ostrm.write('Case #{}: {}\n'.format(caseNum, winner))
  def do_case_less_old(self, caseNum):
    ok = [True if ch=='+' else False for ch in self.istrm.readline().strip()]
    N = len(ok)
    s0 = State(ok)
    winner = None
    flips = 0
    while winner is None:
      flips += 1
      s0.do_all_flips(flips)
      winner = s0.got_a_winner()
      
    self.ostrm.write('Case #{}: {}\n'.format(caseNum, winner))

  def do_case_old(self, caseNum):
    ok = [True if ch=='+' else False for ch in self.istrm.readline().strip()]
    N = len(ok)
    # ok[0] is top of the stak
    flips = 0
    while not all(ok):
      n_to_flip = 1 + ok.index(False)
      # print ok, n_to_flip
      ok = [not p for p in reversed(ok[:n_to_flip]) ] + ok[n_to_flip:]
      # print ok
    self.ostrm.write('Case #{}: {}\n'.format(caseNum, flips))

def main():
  dut = Problem(sys.stdin, sys.stdout)
  dut.do_all_cases()

if __name__ == '__main__':
  main()
