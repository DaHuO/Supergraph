t = int(raw_input())
for i in xrange(1, t + 1):
  n = raw_input()
  prev = ""
  answer = 0
  for inst in n:
    if inst == "-" and prev == "":
      answer += 1
    elif inst == "-" and prev == "+":
      answer += 2
    prev = inst

  print "Case #{}: {}".format(i, answer)