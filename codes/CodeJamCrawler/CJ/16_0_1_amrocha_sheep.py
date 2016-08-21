def check(result):
  return (
    0 in result and
    1 in result and
    2 in result and
    3 in result and
    4 in result and
    5 in result and
    6 in result and
    7 in result and
    8 in result and
    9 in result)


def count_sheep(n):
  if n == 0:
    return 'INSOMNIA'
  seen = dict()
  i = 1
  while True:
    cur = n*i
    i+=1
    for digit in str(cur):
      seen[int(digit)] = True

    if check(seen):
      return cur


results = list()
with open('A-large.in', 'r') as f:
  testcases = int(f.readline())
  for line in f:
    results.append(count_sheep(int(line)))

print results

with open('result.txt', 'w') as f:
  for i, res in enumerate(results):
    f.write('Case #'+str(i+1)+': '+str(res)+'\n')
