#!/usr/bin/env python3

import sys

def first_pass(line):
  uniques = []
  if "X" in line:
    line.remove("S")
    line.remove("I")
    line.remove("X")
    uniques.append("6")

  if "Z" in line:
    line.remove("Z")
    line.remove("E")
    line.remove("R")
    line.remove("O")
    uniques.append("0")

  if "W" in line:
    line.remove("T")
    line.remove("W")
    line.remove("O")
    uniques.append("2")

  if "G" in line:
    line.remove("E")
    line.remove("I")
    line.remove("G")
    line.remove("H")
    line.remove("T")
    uniques.append("8")

  if "U" in line:
    line.remove("F")
    line.remove("O")
    line.remove("U")
    line.remove("R")
    uniques.append("4")

  return uniques

def second_pass(line):
  uniques = []
  if "H" in line:
    line.remove("T")
    line.remove("H")
    line.remove("R")
    line.remove("E")
    line.remove("E")
    uniques.append("3")

  if "F" in line:
    line.remove("F")
    line.remove("I")
    line.remove("V")
    line.remove("E")
    uniques.append("5")

  return uniques

def third_pass(line):
  uniques = []
  if "V" in line:
    line.remove("S")
    line.remove("E")
    line.remove("V")
    line.remove("E")
    line.remove("N")
    uniques.append("7")

  if "I" in line:
    line.remove("N")
    line.remove("I")
    line.remove("N")
    line.remove("E")
    uniques.append("9")

  if "O" in line:
    line.remove("O")
    line.remove("N")
    line.remove("E")
    uniques.append("1")

  return uniques

file  = open(sys.argv[1])
total = int(file.readline())

for i in range(1, total + 1):
  line = list(file.readline().rstrip())
  digits = []
  length = len(line)

  while(True):
    length = len(line)
    digits += first_pass(line)
    if (length == len(line)):
      break

  while(True):
    length = len(line)
    digits += second_pass(line)
    if (length == len(line)):
      break

  while(True):
    length = len(line)
    digits += third_pass(line)
    if (length == len(line)):
      break

  print("Case #%d: %s" % (i, "".join(sorted(digits))))