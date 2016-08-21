T = int(raw_input())
for i in range(T):
  pancakes = raw_input()
  alternations = sum(pancakes[i] != pancakes[i+1] for i in range(len(pancakes)-1))
  last_flip = pancakes[-1] == '-'
  print "Case #%s: %s"%(i+1, alternations + last_flip)
