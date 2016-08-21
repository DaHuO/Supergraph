T = int(input())
f = open('sheep.o', 'w')

def printres(i, res):
  f.write('Case #' + str(i+1) + ': '+ str(res) + '\n')

for i in range(T):
  digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
  MAX = 100000000000000000000
  num = int(input())
  if num == 0:
    printres(i, "INSOMNIA")
  else:
    done = False
    j = 1
    while j < MAX:
      next = j*num
      for c in str(next):
        if c in digits:
          digits.remove(c)
      if not digits:
        printres(i, next)
        done = True
        break
      j += 1
    if not done:
      printres(i, "INSOMNIA")

f.close()  