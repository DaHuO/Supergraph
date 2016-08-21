#!/usr/bin/env python

#fin = open('A-sample.txt', 'r')
#fout = open('A-sample-solution.txt', 'w')

fin = open('A-large.in')
fout = open('A-large.out', 'w')
inputline = fin.readline()
#print inputline
numcase = int(inputline)







for i in range (1,numcase+1):
  line = fin.readline().strip().upper()
  wordlen = len(line)
  last_word = ""
  initial = line[0]
  last_word += initial
  for c in range(1, wordlen):
    if line[c] >= initial:
      last_word = line[c] + last_word
      initial = line[c]
    else:
      last_word = last_word + line[c]
  answer_out = "Case #"+str(i)+": "+last_word+"\n"
  fout.write(answer_out)
  #print answer_out
