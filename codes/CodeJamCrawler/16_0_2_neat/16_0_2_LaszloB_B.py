#https://code.google.com/codejam/contest/6254486/dashboard#s=p1
import time

path = 'B-large'
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
      s.append('Case #' + str(i+1) + ': ' + str(outputs[i]))
  f.write('\n'.join(s))
  f.close()

 
def solve(problem):
  output = 0;
  prev = '';
  for s in problem:
    if s != prev:
      output += 1
      prev = s
  if problem[-1] == '+':
    output -= 1;    
  return output
  
 
starttime = time.time()
data_raw = readfile(path_input)
del data_raw[0]
problems = []
i = False
for line in data_raw:
  problems.append(line.strip())
  
outputs = map(solve, problems)
writefile(path_output, outputs)
  
print 'running time: ', time.time() - starttime