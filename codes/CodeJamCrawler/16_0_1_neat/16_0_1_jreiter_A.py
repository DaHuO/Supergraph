# A.py (Counting Sheep)
# jreiter

for tc in range(int(input())):
  nString = input()
  n = int(nString)
  total = 0
  seendigits =  set(nString)

  if n == 0:
    print("Case #{}: {}".format(tc+1, "INSOMNIA"))
    continue

  while len(seendigits) != 10:
    total += n
    seendigits = seendigits.union(set(str(total)))

  print("Case #{}: {}".format(tc+1, total))