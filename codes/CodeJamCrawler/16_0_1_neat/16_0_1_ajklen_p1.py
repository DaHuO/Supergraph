#!/usr/bin/python3
from sys import stdin

for i in range(int(stdin.readline().strip())):
  digits = [int(x) for x in reversed(stdin.readline().strip())]
  value = [x for x in digits]
  if len([x for x in digits if x != 0]) == 0:
    print("Case #%d: INSOMNIA" %(i+1))
    continue

  seen = [(1 if x in value else 0) for x in range(10)]
  while not all(seen):
    carry = 0
    for j in range(len(value)):
      val = value[j] + carry + (digits[j] if j < len(digits) else 0)
      value[j] = int(val%10)
      seen[value[j]] = 1
      carry = int(val/10)
    if carry != 0:
      value.append(carry)
      seen[carry] = 1
  print("Case #%d: %s" %(i+1, "".join(map(str, reversed(value)))))

