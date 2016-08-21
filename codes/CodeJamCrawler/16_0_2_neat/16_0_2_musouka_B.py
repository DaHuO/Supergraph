#!/usr/bin/env python

#fin = open('B-sample.txt', 'r')
#fout = open('B-sample-solution.txt', 'w')

fin = open('B-large.in')
fout = open('B-large.out', 'w')
inputline = fin.readline()
#print inputline
numcase = int(inputline)


def flip_pcakes(pcakes):
  flipped = ""
  if pcakes == "":
    return ""
  else:
    pcakes = pcakes[::-1]
    for i in range(0, len(pcakes)):
      if pcakes[i] == '-':
        flipped += "+"
      else:
        flipped += "-"

  return flipped
    
# Top is always + 
def find_length_positive_top(pcakes):
  for i in range(0, len(pcakes)):
    if pcakes[i] == "-":
      return i 


# returns number of minimum flips to get all + side up pancakes
def calc_flips(pcakes):
  bottom = len(pcakes)
  num_flips = 0
  if "-" not in pcakes:
    return 0
  elif pcakes == "-":
    return 1
  else:
    #print "Pancakes->" + pcakes + "<-"
    if pcakes[bottom-1] == '+':
      #print "  ==Bottom already +=="
      return calc_flips(pcakes[:-1])
    else:
      #print "  == Bottom is - =="
      if pcakes[0] == "-":
        #print "B:" + pcakes
        new_pcakes = flip_pcakes(pcakes)
        #print "A:" + new_pcakes
        num_flips += 1 + calc_flips(new_pcakes)
      else:
        top_to_flip = find_length_positive_top(pcakes)
        #print " == top to flip:" + str(top_to_flip)
        num_flips += 1
        pcakes = flip_pcakes(pcakes[:top_to_flip]) + pcakes[top_to_flip:]
        num_flips += calc_flips(pcakes)
  return num_flips




for i in range (1,numcase+1):
  line = fin.readline()
  num_flips = calc_flips(line.strip())

  answer_out = "Case #"+str(i)+": "+str(num_flips)+"\n"
  fout.write(answer_out)
  print answer_out
