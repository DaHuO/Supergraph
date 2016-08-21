# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
f = open("A-large.in","r")
x = open("result_large.out","w")
t = int(f.readline())
#t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  n =  int(f.readline())
  result = [0,0,0,0,0,0,0,0,0,0]
  counter = 1
  while counter < 10000:
  	k = counter*n
  	r = str(k)
  	for p in xrange(0,len(r)):
  		result[int(r[p])] = 1
  	if sum(result) == 10:
  		#print "Case #{}: {}".format(i, r)
  		x.writelines("Case #{}: {}\n".format(i, r))
  		break
  	counter += 1
  	if counter == 100:
  		x.writelines("Case #{}: {}\n".format(i, 'INSOMNIA'))
  		#print "Case #{}: {}".format(i, 'INSOMNIA')


  # check out .format's specification for more formatting options

