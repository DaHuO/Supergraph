def bleatrix(N):
  d = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
  def count(x):
    value = []
    for i in d.values():
      value.append(i)

    return value.count(0)

  for i in range(1,100000):
    trigger = i
    value= []
    n = N *i
    a = [int(i) for i in str(n)]
    for i in a:
      d[i] += 1
    if count(d) == 0:
      break
    
  if trigger == 99999:
    return str("INSOMNIA")
  else:
    return n
 
file = open("A-large.in",'r')
l = int(file.readline())
temp = [int (x) for x in file.read().splitlines()]
for i in range (l):
    print("CASE #"+ str(i+1) +': '+ str(bleatrix(temp[i])))

    
