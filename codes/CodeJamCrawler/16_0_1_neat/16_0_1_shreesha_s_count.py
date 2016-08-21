t = int(raw_input())
for i in range(t):
  n = int(raw_input())
  numb = set([])
  if n>0:
    flag = 1
    done = 0
    while(flag > 0):
      temp = flag * n
      lis = map(int, list(str(temp)))
      for j in lis:
        numb.add(j)
        if len(numb) == 10:
          done = 1
          break
      if done == 1:
        print "Case #%d:"% (i+1),
        print temp
        break
      flag += 1
  else:
    print "Case #%d: INSOMNIA" % (i+1)

