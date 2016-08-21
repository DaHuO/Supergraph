#!/usr/bin/python

def condense(stack):
  prev = ''
  result = []
  for c in stack:
    if c != prev:
      result.append(c)
      prev = c

  return result

def process_input(stack):
  result = 0

  while len(stack) > 1:
    stack = condense(stack)

    if stack[0] == '-':
      stack[0] = '+'
      result += 1

    elif len(stack) > 1:
      stack[0] = '-'
      stack[1] = '+'
      result += 1

  if stack[0] == '-':
    return str(result + 1)

  return str(result)

def main():
  T = int(raw_input())
  for t in range(1, T +1):
    stack = raw_input()
    result = process_input(stack)
    print 'Case #' + str(t) + ': ' + result

if __name__ == '__main__':
  main()