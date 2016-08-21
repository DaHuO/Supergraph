def f(s):
    res = ""
    for c in s:
        res = max(res + c, c + res)
    return res

t = int(input())
for i in range(1, t + 1):
  s = input()
  print("Case #{}: {}".format(i, f(s)))
