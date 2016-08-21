# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def add(n, found):
   while(n != 0):
     found.add(n%10)
     n = n/10	
   return found

def findLastNum(num):
   if (num == 0):
	return "INSOMNIA"
   curr_num = num
   found = set()
   for i in range(2,100):
	found = add(curr_num, found)
        if (len(found) == 10):
           break
	else:
	   curr_num = i * num
   if (i == 50): 
	return "INSOMNIA"	
   else:
	return curr_num

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())  # read a list of integers, 1 in this case
  print "Case #{}: {}".format(i, findLastNum(n))
  # check out .format's specification for more formatting options




