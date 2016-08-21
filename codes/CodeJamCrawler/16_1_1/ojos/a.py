#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
  print "Case #%d:" % (nnn),
  S = raw_input().strip()
  word = S[0]
  for s in S[1:]:
    if s > word[0]:
      word = s + word
    elif s < word[0]:
      word += s
    else:
      done = False
      for c in word:
        if s > c:
          word = s + word
          done = True
          break
        elif s < c:
          word += s
          done = True
          break
      if not done:
        word += s
  print word

