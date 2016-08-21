import sys

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
    word = sys.stdin.readline().strip()
    out_word = None
    for ch in word:
      # print ch, ord(ch), out_word
      if out_word is None:
        out_word = ch
      elif ord(ch) < ord(out_word[0]):
        out_word = out_word+ ch
      else:
        out_word = ch  + out_word 
    sys.stdout.write('Case #{}: {}\n'.format(self.case_num, out_word))

def main():
  ProblemSet().do_all_cases()
  

main()
