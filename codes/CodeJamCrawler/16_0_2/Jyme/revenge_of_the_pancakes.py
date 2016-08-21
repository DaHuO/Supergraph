def pack(li):
    p = list()
    last = ''
    for i in li:
      if i != last:
        p.append(i)
        last = i
    if p[-1] == '+':
      del p[-1]
    return p
case = 1
target = open('out', 'w')
with open('input') as f:
  next(f)
  for pancakes in f:
    pancakes = pack(pancakes.strip())
    output = "Case #"+str(case)+": "+str(len(pancakes))
    print output
    target.write(output)
    target.write("\n")
    case+=1
target.close()
