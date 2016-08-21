#!/usr/bin/python3.4

import sys

def count(nb, case):
  nb = int(nb)
  f = open("count_sheep.txt", 'a')
  numbers = set()
  i = 1
  src = nb
  while True:
    i += 1
    str_nb = str(nb)
    for j in range(len(str_nb)):
      numbers.add(str_nb[j])
    a = 0
    for j in numbers:
      a += 1
    if a == 10:
      f.write("Case #" + str(case) + ": " + str_nb + "\n")
      f.close()
      return
    nb = src * i
    if nb == src:
      f.write("Case #" + str(case) + ": INSOMNIA\n")
      f.close()
      return
  f.close()

f = open("count_sheep.txt", "w")
f.write("")
f.close()

t = int(input())
for i in range(1, t + 1):
  n = int(input())
  count(n, i)
