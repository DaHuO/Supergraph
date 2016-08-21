#! /usr/bin/env python
import sets

o = open('output.txt', "w")
o.close()
with open('A-large.in', 'r') as f:
  for i, line in enumerate(f.readlines()):
    if i == 0:
      print '%d test cases' % int(line)
      continue
    o = open('output.txt', "a")
    start = int(line)
    char_seen = sets.Set(list(str(start)))
    solution = 1
    if start == 0:
      value = "INSOMNIA"
    else:
      while len(char_seen) < 10:
        solution += 1
        value = str(start * solution)
        char_seen.update(list(value))

    o.write('Case #%d: %s' % (i, value))
    o.write('\n')
    o.close()
