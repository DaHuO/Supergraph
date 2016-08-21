import fileinput
import itertools

# k committee members starting from index n need to say yes
def get_probability_recur(l, n, k, memo):
  if k < 0:
    return 0.0
  elif n == len(l):
    if k == 0:
      return 1.0
    else:
      return 0.0
  if memo[n][k] < 0:
    memo[n][k] = (l[n] * get_probability_recur(l, n+1, k-1, memo) +
                  (1 - l[n]) * get_probability_recur(l, n+1, k, memo))
  return memo[n][k]

def get_probability(l):
  k = len(l)
  memo = [[-1.0]*(k+1) for i in range(k+1)]
  return get_probability_recur(l,0,k/2,memo)

num_cases = int(raw_input())
for case in range(1,num_cases+1):
  inputs = raw_input().split()
  N = int(inputs[0])
  k = int(inputs[1])
  inputs = raw_input().split()
  probs = [float(x) for x in inputs]
  best_prob = -1
  for subset in itertools.combinations(probs,k):
    cur_prob = get_probability(list(subset))
    if cur_prob > best_prob:
      best_prob = cur_prob
  print("Case #%d: %f" % (case, best_prob))
