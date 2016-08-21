# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  inputStr = raw_input().strip()  # read a list of integers, 2 in this case
  outputStr = ''
  lastCh = inputStr[0]
  for inputCh in inputStr:
  	if (inputCh < lastCh):
  		outputStr = outputStr + inputCh
  	else:
  		outputStr = inputCh + outputStr 
  	lastCh = outputStr[0]
  print("Case #{}: {}".format(i, outputStr))
  # check out .format's specification for more formatting options