t = int(raw_input())
inputs = []

for x in range(t):
    inputs.append(raw_input())


for n, s in enumerate(inputs):
    first = s[0]
    answer = first
    for x in s[1:]:
      if x >= first:
        answer = x + answer
        first = x
      else:
        answer = answer + x

    print "Case #%r: %s" % (n+1, answer)