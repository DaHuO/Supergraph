#!/usr/bin/env python3

import sys

DEBUG = False

def main():
  if len(sys.argv) != 2:
    print("Usage: %s <input file>" % sys.argv[0])
    sys.exit(0)
  
  with open(sys.argv[1], 'r') as f:
    num_cases = int(f.readline())

    for case_num in range(num_cases):
      digits = set()
      seed = int(f.readline())
      mult = 1
      asleep = False
      insomnia = False

      while not (asleep or insomnia):
        # calculate the current number
        last_num = seed * mult
        
        count = len(digits)
        [digits.add(digit) for digit in str(last_num)]
        if DEBUG: print(("Last: %d - Digits:" % last_num), digits)

        # If we have all 10 digits, Bleatrix is asleep
        if len(digits) == 10:
          asleep = True
          if DEBUG: print("ASLEEP")
        # If the number of digits grew, but we don't have 10 yet
        elif len(digits) > count:
          rounds_since_add = 0
        # If the number is not changing (Only occurs if input was 0)
        elif last_num == seed:
          insomnia = True

        # Move onto the next multiplier
        mult += 1


      if asleep:
        result = last_num
      elif insomnia:
        result = "INSOMNIA"
      else:
        result = "ERROR"

      print("Case #%d: %s" % (case_num + 1, result))


if __name__ == "__main__":
  main()
