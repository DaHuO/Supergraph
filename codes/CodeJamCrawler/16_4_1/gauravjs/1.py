def order2(p,order):
  ordering = []
  if order == 0:
    ordering = ['P', 'R', 'S']
  if order == 1:
    ordering = ['P', 'S', 'R']
  if order == 2:
    ordering = ['S', 'P', 'R']
  if order == 3:
    ordering = ['S', 'R', 'P']
  if order == 4:
    ordering = ['R', 'S', 'P']
  if order == 5:
    ordering = ['R', 'P', 'S']

  out = []
  for i in range(3):
    if ordering[i] in p:
      out.append(ordering[i])

  return out   

hands = {'P':['P','R'], 'R':['R','S'], 'S':['S','P']}
  

def rps(n,r,p,s,order):
  pnext = 2**(n-1) - s
  rnext = 2**(n-1) - p
  snext = 2**(n-1) - r

  if pnext < 0 or rnext < 0 or snext < 0:
    return 'IMPOSSIBLE'

  if n == 1:
    if pnext:
      return order2(['P','R'],order)
    if rnext:
      return order2(['R','S'],order)
    if snext:
      return order2(['P','S'],order)

  recurse = rps(n-1,rnext,pnext,snext,(order+1)%6)

  if recurse == 'IMPOSSIBLE':
    return 'IMPOSSIBLE'
  else:
    out = []
    for i in recurse:
      out += order2(hands[i], order)

  return out



with open('A-large.in','r') as f:
    cases=int(f.readline())
    lines=f.readlines()

for i in range(cases):
  n,r,p,s=map(int,lines[i].strip().split(' '))
  print "Case #" + str(i+1) + ": " + ''.join(rps(n,r,p,s,0))
