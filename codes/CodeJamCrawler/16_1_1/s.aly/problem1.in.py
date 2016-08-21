# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.


from itertools import permutations 

#fin = open("sample.in","r")
fin = open("A-large.in","r")
fout = open("sample.out","w")

t = int(fin.readline())  # read a line with a single integer
for v in range(1, t + 1):
  x=fin.readline()
  x=x.strip()
##  for s in x.split(" "):
##      n= list(s.strip())
##  n.sort()
  lst = []
  for i in x:
      if len(lst)==0:
          lst.append(i)
      elif i>=lst[0]:
          lst.insert(0,i)
      else:
          lst.append(i)
  print("Case #{}: {}".format(v,''.join(lst)))
  fout.write("Case #{}: {}".format(v,''.join(lst)))
  fout.write("\n")
fout.close()
  # check out .format's specification for more formatting options
