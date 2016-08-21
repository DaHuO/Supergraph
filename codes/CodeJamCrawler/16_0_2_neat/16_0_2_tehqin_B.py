
opp = {'+':'-', '-':'+'}
T = int(raw_input())
for tc in range(1, T+1):
   s = raw_input()
      
   res = 0
   while '-' in s:
      i = s.find(opp[s[0]])-1 if '+' in s else len(s)-1
      s = s[:i+1][::-1].replace(s[0], opp[s[0]]) + s[i+1:]
      res += 1
   print 'Case #{}: {}'.format(tc, res)
