#!/usr/bin/python

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
strings = [('Z','ZERO'),('W','TWO'),('U','FOUR'),('R','THREE'),('X','SIX'),('S','SEVEN'),('H','EIGHT'),('O','ONE'),('V','FIVE'),('N','NINE')]
numbers = {'Z': '0', 'W': '2', 'U': '4', 'R': '3', 'X': '6', 'S': '7','H':'8','O':'1','V':'5','N': '9'}
for i in xrange(1, t + 1):
  chars = raw_input()
  
  values = []
  
  for value in strings:
  	key = value[0]
  	value = value[1]

  	while chars.find(key) != -1:
  	  for j in xrange(0, len(value)):
  	    chars = chars.replace(value[j],'',1)
  	  values.append(numbers[key])
  	  
  values.sort()
  
  print "Case #{}: {}".format(str(i), ''.join(values))
  # check out .format's specification for more formatting options