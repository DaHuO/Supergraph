import sys
import re
import random
ctr = -1
alpha = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
with open(sys.argv[1]) as f:
  for line in f:
    ctr += 1
    if ctr == 0:
      continue
    line = line.strip()
    s = line
    num = ""
    while(1):
      if "Z" in s:
        num += str(0)
        s = s.replace("Z", "", 1)
        s = s.replace("E", "", 1)
        s = s.replace("R", "", 1)
        s = s.replace("O", "", 1)
      else:
        break
    while(1):
      if "W" in s:
        num += str(2)
        s = s.replace("T", "", 1)
        s = s.replace("W", "", 1)
        s = s.replace("O", "", 1)
      else:
        break
    while(1):
      if "U" in s:
        num += str(4)
        s = s.replace("F", "", 1)
        s = s.replace("O", "", 1)
        s = s.replace("U", "", 1)
        s = s.replace("R", "", 1)
      else:
        break
    while(1):
      if "X" in s:
        num += str(6)
        s = s.replace("S", "", 1)
        s = s.replace("I", "", 1)
        s = s.replace("X", "", 1)
      else:
        break
    while(1):
      if "G" in s:
        num += str(8)
        s = s.replace("E", "", 1)
        s = s.replace("I", "", 1)
        s = s.replace("G", "", 1)
        s = s.replace("H", "", 1)
        s = s.replace("T", "", 1)
      else:
        break
    while(1):
      if "O" in s:
        num += str(1)
        s = s.replace("O", "", 1)
        s = s.replace("N", "", 1)
        s = s.replace("E", "", 1)
      else:
        break
    while(1):
      if "H" in s:
        num += str(3)
        s = s.replace("T", "", 1)
        s = s.replace("H", "", 1)
        s = s.replace("R", "", 1)
        s = s.replace("E", "", 1)
        s = s.replace("E", "", 1)
      else:
        break
    while(1):
      if "F" in s:
        num += str(5)
        s = s.replace("F", "", 1)
        s = s.replace("I", "", 1)
        s = s.replace("V", "", 1)
        s = s.replace("E", "", 1)
      else:
        break
    while(1):
      if "V" in s:
        num += str(7)
        s = s.replace("S", "", 1)
        s = s.replace("E", "", 1)
        s = s.replace("V", "", 1)
        s = s.replace("E", "", 1)
        s = s.replace("N", "", 1)
      else:
        break
    while(1):
      if "N" in s:
        num += str(9)
        s = s.replace("N", "", 1)
        s = s.replace("I", "", 1)
        s = s.replace("N", "", 1)
        s = s.replace("E", "", 1)
      else:
        break

    print "Case #%d: %s" %(ctr, ''.join(sorted(num)))



