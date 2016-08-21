#https://code.google.com/codejam/contest/6254486/dashboard#s=p0
import time

path_input = 'A-large.in'
path_output = 'A-large.out'

def readfile(path):
  with open(path, 'r') as f:
    data_raw = f.readlines()
  f.closed
  return data_raw

def writefile(path, outputs):
  f = open(path, 'w')
  s = []
  for i in range(len(outputs)):
      s.append('Case #' + str(i+1) + ': ' + str(outputs[i]))
  f.write('\n'.join(s))
  f.close()

 
def solve(problem):
  digits = {}
  N = 0
  i = 0
  while len(digits) < 10 and i < 1000000:
    N += problem
    sN = str(N)
    for s in sN:
      digits[s] = True
    i += 1

  if i == 1000000:
    N = 'INSOMNIA'
  return N
  
 
starttime = time.time()
data_raw = readfile(path_input)
del data_raw[0]
problems = []
i = False
for line in data_raw:
  line = map(int, line.strip().split(' '));
  problems.append(line[0])
  
outputs = map(solve, problems)
writefile(path_output, outputs)
  
print 'running time: ', time.time() - starttime