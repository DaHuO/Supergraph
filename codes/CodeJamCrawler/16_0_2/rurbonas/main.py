import sys

def solve_subcase_for(s, c):
  result = 0
  
  if len(s) > 1:
    result += solve_subcase_for(s[:-1], s[-1])
    
  result += 0 if s[-1] == c else 1
  
  return result

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  line = infile.readline().strip()
  result = solve_subcase_for(line, '+')

  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  print result
  
infile.close()