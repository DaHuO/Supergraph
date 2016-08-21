T = input()
for i in range(T):
  K, C, S = [int(x) for x in raw_input().split()]
  answer = ' '.join([str(x) for x in range(1,K+1)])
  print "Case #%s: %s"%(i+1, answer)
