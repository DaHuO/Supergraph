import sys

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(":")
  
  K, C, S = [int(v) for v in infile.readline().split()]
  
  for i in range(K):
    sys.stdout.write(" " + str(i+1))
  print
  
infile.close()