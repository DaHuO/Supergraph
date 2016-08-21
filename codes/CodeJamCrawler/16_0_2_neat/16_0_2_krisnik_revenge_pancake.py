__author__ = 'KH2006'

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
# print "number of test cases ",t
for i in xrange(1, t + 1):
  inputForTestCase = raw_input()  # read a test case
  output = 0
  lengthStr = len(inputForTestCase)
  while True:
      # find the + patterns from back
      count = lengthStr - 1
      while count >= 0:
          if inputForTestCase[count] == "-":
              break
          count -= 1
      # now flip from 0 to count.
      if count == -1:
          break

      listStr = list(inputForTestCase)
      for j in range(count + 1):
          if listStr[j] == "+":
              listStr[j] = "-"
          else:
              listStr[j] = "+"
      inputForTestCase = ''.join(listStr)
      output += 1

  print "Case #{}: {}".format(i, output)
  # check out .format's specification for more formatting options

