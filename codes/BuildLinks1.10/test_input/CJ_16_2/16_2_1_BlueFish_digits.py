def solve(s):
 d=[0]*10
 d[0]=s.count('Z')
 d[6]=s.count('X')
 d[2]=s.count('W')
 d[4]=s.count('U')
 d[8]=s.count('G')
 d[7]=s.count('S')-d[6]
 d[5]=s.count('V')-d[7]
 d[4]=s.count('F')-d[5]
 d[3]=s.count('H')-d[8]
 d[1]=s.count('O')-d[0]-d[2]-d[4]
 d[9]=s.count('I')-d[5]-d[6]-d[8]
 out=reduce(lambda x,y: x+y, [[i]*d[i] for i in range(10)])
 out=''.join([str(x) for x in out])
 return out

inp=file('A-large.in','rb+'); out=file('A-large.out','wb+')

T=int(inp.readline().strip())

for x in range(1,T+1): out.write('Case #%i: %s\r\n'%(x,solve(inp.readline().strip())))