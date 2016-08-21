# D.py (Fractiles)
# jreiter

for tc in range(int(input())):
  k, c, s = [int(x) for x in input().split()]

  tileString = " ".join(str(x) for x in range(1, k+1))

  print("Case #{}: {}".format(tc+1, tileString))