# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())
  groups = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  str_to_out=""
  while (max(groups)>0):
    first_index = groups.index(max(groups))
    groups[first_index] = groups[first_index] - 1
    second_index=-1
    if (max(groups)>0 and sum(groups)!=2):
      second_index = groups.index(max(groups))
      groups[second_index] = groups[second_index] - 1
    str_to_out += chr(first_index+ord('A'))
    if second_index!=-1:
      str_to_out=str_to_out+chr(second_index+ord('A'))
    if (max(groups)>0):
	  str_to_out = str_to_out + " "
  print "Case #{}: {}".format(i, str(str_to_out))
  
  #print "Case #{}: {} {}".format(i, n + m, n * m)
  # check out .format's specification for more formatting options