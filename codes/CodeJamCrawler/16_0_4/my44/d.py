t = int(raw_input())
lines = [0 for i in range(t)]
for i in range(t):
  lines[i] = map(int, raw_input().split())
ans = [None for i in range(t)]
for idx, line in enumerate(lines):
  k, c, s = line
  ans[idx] = range(1, k+1)

for idx, value in enumerate(ans):
  if type(value) == list:
    outstr = "Case #{0}: {1}".format(idx+1, " ".join(map(str, value)))
  else:
    outstr = "Case #{0}: {1}".format(idx+1, value)
  print(outstr)
