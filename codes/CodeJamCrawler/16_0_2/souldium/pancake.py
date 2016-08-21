f = open('input', 'r');
n = int(f.readline())
for i in range(n):
 s = f.readline()
 ans = 0 if s[-2]=='+' else 1
 n = len(s)
 temp = s[0]
 for j in range(1,n-1):
  if temp != s[j]:
   ans += 1;
   temp = s[j];
 print 'Case #%d: %d' %(i+1, ans)
