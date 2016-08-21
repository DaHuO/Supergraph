__author__ = 'Nikhil'

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
# print "number of test cases ",t
for i in xrange(1, t + 1):
  inputForTestCase = raw_input()  # read a test case
  myDict = {}
  if inputForTestCase == "0":
      output = "INSOMNIA"
  else:
      count = 1
      while len(myDict.keys()) < 10:
          output = str(int(inputForTestCase) * count)
          # print "updating dict with inputForTestCase ",output," its type ", type(output)
          for s in output:
              myDict[s] = "true"
          count += 1

  print "Case #{}: {}".format(i, output)
  # check out .format's specification for more formatting options
