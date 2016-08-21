#!/usr/bin/env python3

import sys

DEBUG = False

def flip(stack_in, count = 0):
  if DEBUG: print("Stack in:", stack_in)

  if count == 0:
    count = len(stack_in)
  if DEBUG: print("Num to flip:", count)
  
  # Extract the portion to be flipped
  to_flip = stack_in[:count]
  if DEBUG: print("To Flip:", to_flip)

  # Flip and reverse the extracted stack portion
  flipped = [not(state) for state in to_flip[::-1]]
  if DEBUG: print("Part Flip:", flipped)

  # Add the unflipped portion to the list
  flipped.extend(stack_in[count:])
  if DEBUG: print("Stack out:", flipped)

  return flipped


def main():
  if len(sys.argv) != 2:
    print("Usage: %s <input file>" % sys.argv[0])
    sys.exit(0)
  
  with open(sys.argv[1], 'r') as f:
    num_cases = int(f.readline())

    for case_num in range(num_cases):
      # Get the string describing the stack
      in_str = f.readline().strip()

      # Initialise a list to represent the stack
      stack = []

      # Loop through each item in the stack
      for i in range(len(in_str)):
        # Store stack item as boolean for face-up
        if in_str[i] == "+":
          stack.append(True)
        else:
          stack.append(False)
      if DEBUG: print("Initial:", stack)

      # Initialise the number of flips
      num_flips = 0

      # Flip pancakes from top to bottom
      for i in range(len(stack) - 1) :
        # Flip if different from next pancake
        if stack[i] != stack[i + 1]:
          stack = flip(stack, i + 1)
          num_flips += 1
      
      #  Flip the whole stack if face down
      if stack[0] == False:
        stack = flip(stack)
        num_flips += 1
      
      if DEBUG: print("Final:", stack)

        
      print("Case #%d: %d" % (case_num + 1, num_flips))


if __name__ == "__main__":
  main()
