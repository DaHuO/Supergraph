# imports



# code
def digits(n):
  d = set()
  while n > 0:
    bit = n % 10
    if not bit in d:
      d.add(bit)
    n = n // 10
  return d

def sheep(n):
  if n == 0:
    return -1
  marked = [False for _ in xrange(10)]
  mark_count = 0
  a = n
  while mark_count < 10:
    what_digits = digits(a)
    for bit in what_digits:
      if not marked[bit]:
	marked[bit] = True
	mark_count += 1
    a += n
  return a - n

if __name__ == "__main__":
  g = open("output", "w")
  with open("A-large.in") as f:
    num_cases = 0
    read_num_cases = False
    c = 1
    for line in f:
      if not read_num_cases:
	read_num_cases = True
	num_cases = int(line)
      else:
	n = int(line)
	res = sheep(n)
	g.write("Case #" + str(c) + ": " + (str(res) if res >= 0 else "INSOMNIA") + "\n")
	c += 1
  g.close()