import sys as S

def f(case_number, n):
  seen = set()

  s = str(n)

  for i in range(10**(len(s)+1)):
    for d in str(n*(i + 1)):
      seen.add(d)
    if len(seen) == 10:
      break

  if len(seen) == 10:
    print 'Case #' + str(case_number) + ': ' + str(n * (i + 1))
  else:
    print 'Case #' + str(case_number) + ': INSOMNIA'

i = 0
for line in S.stdin:
  i += 1
  if i == 1:
    continue
  f(i-1, int(line))

