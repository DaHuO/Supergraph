def f(ls, n):
    guards = []
    res = set([])
    for l in ls:
        for elt in l:
            guards.append(elt)
    for elt in guards:
        if guards.count(elt) % 2 != 0:
            res.add(elt)
    return ' '.join([str(x) for x in sorted(list(res))])

t = int(input())
for i in range(1, t + 1):
  n = int(input())
  lists = []
  for j in range(2 * n - 1):
      lists.append([int(x) for x in input().split(' ')])
  print("Case #{}: {}".format(i, f(lists, n)))
