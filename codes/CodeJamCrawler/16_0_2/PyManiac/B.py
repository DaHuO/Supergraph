def get_ans(s):
  ans = 0
  while s.endswith('+') : s = s[:-1]
  while s != '' :
    x = []
    for i in range(len(s)):
      if s[i] == '-' :
        x.append('+')
      else:
        x.append('-')
    s = ''.join(x)
    while s.endswith('+') : s = s[:-1]
    if s == '+' : s = ''
    ans += 1
  return ans

fp = open('a.in' , 'r')
fout = open('a.out' , 'w+')

for i in range(int(fp.readline())):
  s = fp.readline().replace('\n' , '')
  ans = get_ans(s)
  fout.writelines("Case #" + str(i+1) + ": " + str(ans) + '\n')

fp.close()
fout.close()
