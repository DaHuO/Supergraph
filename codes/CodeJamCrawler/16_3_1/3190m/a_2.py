# -*- coding: utf-8 -*-

# Round 1C 2016
# Problem A.

T = int(input())
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def calc(N, Ps):
  if N == 2:
    return " ".join(["AB"] * Ps[0])
  if N > 2:
    plan = []
    while sum(Ps) > 0:
      if sum(Ps) == 2:
        plan.append(alphabet[N-2] + alphabet[N-1])
        Ps = [0 for p in Ps]
      else:
        for k in range(N):
          if Ps[k] == max(Ps):
            plan.append(alphabet[k])
            Ps[k] = Ps[k] - 1
            break

    return " ".join(plan)

for i in range(T):
  N = int(input())
  Ps = [int(p) for p in input().split(" ")]
  a = calc(N, Ps)
  print("Case #{}: {}".format(i + 1, a))