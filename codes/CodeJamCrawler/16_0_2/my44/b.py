t = int(raw_input())
lines = [0 for i in range(t)]
for i in range(t):
  lines[i] = raw_input()
ans = [None for i in range(t)]
for idx, state in enumerate(lines):
  cnt = 0
  tmpstate = list(state)
  while True:
    if not ("-" in tmpstate):
      ans[idx] = cnt
      break
    len_ts = len(tmpstate)
    if tmpstate[-1] == "-":
      if tmpstate[0] == "-":
        tmpstate = ["-" if tmpstate[len_ts-1-i] == "+" else "+" for i in range(len_ts-1)]
        cnt += 1
      else:
        blankside = tmpstate.index("-")
        tmpstate = ["-" if tmpstate[blankside-1-i] == "+" else "+" for i in range(blankside)] + tmpstate[blankside:]
        tmpstate = ["-" if tmpstate[len_ts-1-i] == "+" else "+" for i in range(len_ts-1)]
        cnt += 2
    else:
      tmpstate = tmpstate[:-1]


for idx, num in enumerate(ans):
  outstr = "Case #{0}: {1}".format(idx+1, num)
  print(outstr)
