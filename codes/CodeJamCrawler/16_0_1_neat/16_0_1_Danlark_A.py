s1 = set()


def check(a):
  s = str(a)
  for i in range(len(s)):
    s1.add(int(s[i]))
a = ['INSOMNIA']
for i in range(1, 10**6 + 1):
  j = i
  k = 2
  s1 = set()
  while (len(s1) < 10):
    check(j)
    j = i * k
    k += 1
  a.append(j - i)

inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
t = int(inf.readline())

for i in range(1, t + 1):
  c = int(inf.readline())
  print('Case #', i, ': ', a[c], sep = '', file = ouf)

inf.close()
ouf.close()
