tr = dict({'pr':'p','rp':'p','ps':'s','sp':'s','rs':'r','sr':'r'})
def RPS(n,r,p,s,od):
  if n == 0:
    res = 'R'*r+'P'*p+'S'*s
    return res
  r1,s1,p1 = (r+s-p)/2,(s+p-r)/2,(p+r-s)/2
  if r1 < 0 or p1 < 0 or s1 < 0:
    return 'IMPOSSIBLE'
  od1 = tr[od[0]+od[1]]+tr[od[0]+od[2]]+tr[od[1]+od[2]]
  res1 = RPS(n-1,r1,p1,s1,od1)
  if res1 == 'IMPOSSIBLE':
    return res1
  res = res1.replace('R',od.replace('p','')).replace('S',od.replace('r','')).replace('P',od.replace('s',''))
  return res.upper()


t = int(raw_input())
for i in range(1,t+1):
  n,r,p,s = map(int,raw_input().split())
  print 'Case #%d: %s' % (i,RPS(n,r,p,s,'prs'))
