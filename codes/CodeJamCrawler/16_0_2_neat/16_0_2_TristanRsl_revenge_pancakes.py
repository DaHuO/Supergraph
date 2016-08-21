#!/usr/bin/python3.4

def return_pancake(stack, index):
  for i in range(0, index + 1):
    if stack[i] == "-":
      stack[i] = "+"
    else:
      stack[i] = "-"
  return stack

def pancake(src, case):
  stack = []
  step = 0
  f = open("pancake.txt", 'a')
  for char in src:
    stack.append(char)
  for i in range(len(stack) - 1, -1, -1):
    if stack[i] == "-":
      return_pancake(stack, i)
      step += 1
  f.write("Case #" + str(case) + ": " + str(step) + "\n")
  f.close() 

f = open("pancake.txt", "w")
f.write("")
f.close()

t = int(input())
for i in range(1, t + 1):
  n = str(input())
  pancake(n, i)
