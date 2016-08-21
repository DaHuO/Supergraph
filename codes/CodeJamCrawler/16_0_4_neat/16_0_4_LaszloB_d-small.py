#https://code.google.com/codejam/contest/6254486/dashboard#s=p3
import time


path = 'D-small-attempt1'
path_input = path + '.in'
path_output = path + '.out'

def readfile(path):
  with open(path, 'r') as f:
    data_raw = f.readlines()
  f.closed
  return data_raw

def writefile(path, outputs):
  f = open(path, 'w')
  s = []
  for i in range(len(outputs)):
      s.append('Case #' + str(i+1) + ': ' + ' '.join(map(str, outputs[i])))
  f.write('\n'.join(s))
  f.close()

 
def solve(problem):
  K, C, S = problem
  return range(1, K+1)
  
 
starttime = time.time()
data_raw = readfile(path_input)
del data_raw[0]
problems = []
i = False
for line in data_raw:
  line = map(int, line.strip().split(' '));
  problems.append(line)
  
outputs = map(solve, problems)
writefile(path_output, outputs)
  
print 'running time: ', time.time() - starttime