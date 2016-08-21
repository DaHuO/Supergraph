tn = input()
ti = 0

p1 = ['ZERO', 'TWO', 'FOUR', 'SIX', 'EIGHT']
p2 = ['ONE', 'THREE', 'FIVE', 'SEVEN', 'NINE']

q1 = ['0', '2', '4', '6', '8']
q2 = ['1', '3', '5', '7', '9']

def con():
  a = {}
  for i in range(26):
    a[(chr(ord('A') + i))] = 0
  return a

def take(a, s):
  for x in s:
    a[x] -= 1

  b = True
  for x in a:
    if a[x] < 0: b = False

  if not b:
    for x in s:
      a[x] += 1

  return b

while ti < tn:

  l = ''
  a = con()
  s = raw_input()

  for x in s:
    a[x] += 1

  i = 0
  while i < len(p1):
    b = take(a, p1[i])
    if b:
      l += q1[i]
    if not b:
      i += 1

  i = 0
  while i < len(p2):
    b = take(a, p2[i])
    if b:
      l += q2[i]
    if not b:
      i += 1

  l = ''.join(x for x in sorted(l))

  ti += 1
  print 'Case #%s: %s' % (ti, l)

  for x in a:
    if a[x] != 0: '============ WTF ============'

