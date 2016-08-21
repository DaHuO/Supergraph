import sys

def main():
  t = int(sys.stdin.readline())
  for case in range(1, t+1):
    sys.stderr.write('processing case %d\n' % case)
    process_case(case)
  sys.stderr.write('Finished\n')

def process_case(case):
  stack = str(sys.stdin.readline()).strip()
  groups = []
  for ch in stack:
    if not len(groups) or groups[-1] != ch:
      groups.append(ch)
  count = len(groups)
  if groups[-1] == '+':
    count -= 1

  sys.stdout.write('Case #%d: %d\n' % (case, count))

if __name__ == '__main__':
  main()
