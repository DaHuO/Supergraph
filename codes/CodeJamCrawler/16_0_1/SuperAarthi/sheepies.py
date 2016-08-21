f = open('A-large.in', 'r')
out = open('sheepiesOutput.txt', 'w')

numLines = f.readline()

for i in range(int(numLines)):
  num = f.readline()
  num.rstrip()
  n = int(num)
  
  if n == 0:
    out.write('Case #%d: INSOMNIA\n' % (i+1))
  else:
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    last = 0
    while len(digits) > 0:
      last += n
      strLast = str(last)
      for a in range(len(strLast)):
        if digits.count(strLast[a]) != 0:
          digits.remove(strLast[a])
    out.write('Case #%d: %d\n' % (i+1, last))