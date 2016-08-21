# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
f = open('D-small-attempt0.in', 'r')
fout = open('D-small-attempt0.out', 'w')
t = int(f.readline().split()[0])  # read a line with a single integer

for i in xrange(1, t + 1):
  inlist  = f.readline().split() # read a list of integers, 2 in this case
  K = int(inlist[0])
  C = int(inlist[1])
  S = int(inlist[2])
  res = ""
  numres = pow(K, C-1)
  for q in range(K):
	  res += str(numres + q) + " "
  
  outstr =  "Case #" + str(i) + ": " + res + "\n"
  print outstr
  fout.write(outstr)

  


f.close()
fout.close()

