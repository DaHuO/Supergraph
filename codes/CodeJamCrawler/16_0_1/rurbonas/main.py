import sys

def calculate_result(N):
  if N == 0:
    return "INSOMNIA"
    
  last_value = 0
  check_set = set()
  while 1:
    last_value += N
    check_set.update(str(last_value))
    if (len(check_set) == 10):
      return last_value
  

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  N = int(infile.readline())
  
  print calculate_result(N)
  
infile.close()