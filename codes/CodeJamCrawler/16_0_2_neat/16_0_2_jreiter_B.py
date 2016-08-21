# B.py (Revenge of the Pancakes)
# jreiter

def flipStack(inStr):
  outStr = ""
  for ch in reversed(inStr):
    outStr += "+" if ch == "-" else "-"
  return outStr

for tc in range(int(input())):
  stack = input()
  flips = 0
  prev = "top"

  for p in stack:
    if p != prev and prev != "top":
      flips += 1
    prev = p

  if stack[-1] == "-":
    flips += 1 

  print("Case #{}: {}".format(tc+1, flips))