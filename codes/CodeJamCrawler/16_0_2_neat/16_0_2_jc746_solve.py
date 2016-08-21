#! /usr/bin/env python
import sets

def flip(line, count):
  return ''.join(map(lambda x: '-' if x == '+' else '+', reversed(line[0:count]))) + line[count:]

o = open('output.txt', "w")
o.close()
with open('B-small-attempt2.in', 'r') as f:
  for i, line in enumerate(f.readlines()):
    if i == 0:
      print '%d test cases' % int(line)
      continue
    # Do a BFS. Keep state with flip count and state string.
    queue = [(0, line.strip())]
    seen = [line.strip()]
    while len(queue) > 0:
      state = queue.pop(0)
      if state[1] == ('+' * len(state[1])):
        break
      for j in range(1, len(state[1]) + 1):
        new = (state[0] + 1, flip(state[1], j))
        if not new[1] in seen:
          seen.append(new[1])
          queue.append(new)

    o = open('output.txt', "a")
    value = 0
    o.write('Case #%d: %s' % (i, state[0]))
    o.write('\n')
    o.close()
