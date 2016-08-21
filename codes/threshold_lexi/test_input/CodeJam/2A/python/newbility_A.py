from sys import argv
from collections import defaultdict



def fail(R, P, S):
  s = R + P + S
  s3 = s / 3
  s3p = s3 + 1
  return R < s3 or P < s3 or S < s3 or R > s3p or P > s3p or S > s3p

def output(R, P, S):
  remainder = []
  s = R + P + S
  if s == 1:
    return 'R'*R + 'P'*P + 'S'*S
  s3 = s / 3
  RPS = [R, P, S]
  for i in range(3):
    if RPS[i] > s3:
      remainder.append(i)
  if len(remainder) == 2:
    ret = ''
    if 1 in remainder:
       ret += output(s3/2, s3/2 +1, s3/2)
    if 0 in remainder:
       ret += output(s3/2+1, s3/2, s3/2)
    if 2 in remainder:
       ret += output(s3/2, s3/2, s3/2+1)
    return ret
  ss = s3/4
  PP = output(ss, ss+1, ss)
  RR = output(ss+1, ss, ss)
  SS = output(ss, ss, ss+1)
  if remainder[0] == 0: # R
    return PP + RR + RR + SS
  if remainder[0] == 1: # P
    return PP + RR + PP + SS
  if remainder[0] == 2: # S
    return PP + SS + RR + SS

def foo(a):
  [N,R,P,S] = [int(x) for x in a.split(' ')]
  if fail(R, P, S):
    return "IMPOSSIBLE"
  return output(R, P, S)


# main
lines = [x.strip() for x in open(argv[1]).readlines()]
pos = 0
T = int(lines[pos])
pos+=1
for t in range(1, T+1):
  a = lines[pos]
  pos+=1
  print "case #%d: %s" % (t, foo(a))
