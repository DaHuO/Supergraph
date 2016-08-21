# imports



# code

def pan(stack):
  if len(stack) < 1:
    return 0
  n = 1 if stack[-1] == '-' else 0
  c = stack[0]
  for i in xrange(len(stack) - 1):
    d = stack[i + 1]
    if d != c:
      n += 1
      c = d
  return n

if __name__ == "__main__":
  g = open("output2", "w")
  with open("B-large.in") as f:
    num_cases = 0
    read_num_cases = False
    c = 1
    for line in f:
      if not read_num_cases:
	read_num_cases = True
	num_cases = int(line)
      else:
	g.write("Case #" + str(c) + ": " + str(pan(line[:-1])) + "\n")
	c += 1
  g.close()