fn = "input_cur.in"

f = open(fn, 'r')
data = f.readlines()
f.close()
nentry = data.pop(0)
maxval = 10**6
tdata = []
for d in data:
  tdata.append(int(d))
  

test = ['0','1','2','3','4','5','6','7','8','9']
for d in tdata:
  tmp = []
  for i in range(maxval):
    td = list(str(d*(i+1)))
    for tdd in td:
      if tdd not in tmp:
        tmp.append(tdd)
    if len(tmp) == 10:
      break
  if len(tmp) != 10:
    print 'Case #'+str(tdata.index(d)+1)+': '+ 'INSOMNIA'
  else:    
    print 'Case #'+str(tdata.index(d)+1)+': '+ ''.join(td)      

  
