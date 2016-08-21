import sys

def main(argv):
  t = int(raw_input().strip())

  for ii in xrange(t):
    s = raw_input().strip()
    c = 0
    last_char = None
    index = 0

    ll = []
    while index < len(s):
      ch = s[index]
      while ch == "+":
        if last_char == "-":
          ll.append(last_char)
        last_char = "+"
        index += 1
        if index >- len(s):
          break
        ch = s[index]
        continue

      while ch == "-":
        if last_char == "+":
          ll.append(last_char)
        last_char = "-"
        index += 1
        if index >- len(s):
          break
        ch = s[index]
        continue
    ll.append(last_char)

    ss = "".join(ll)

    if ss[-1] == "+":
      c = len(ss) - 1
    if ss[-1] == "-":
      c = len(ss)

    print "Case #%d: %d" % (ii+1, c)

if __name__ == "__main__":
  main(sys.argv)
