def Bleatrix(N):
  digits = []
  temp = N
  size = 0
  i = 1
  while(size != 10):
    last = i * N
    if(temp == 0):
          return 0

    if(digits.__contains__(temp%10) == False):
        digits.append(temp%10)

    size = 0
    for x in range(0, 10):
      if(digits.__contains__(x) == True):
        size += 1
      else:
        break
    temp = temp // 10
    if(temp  == 0):
        i += 1
        temp = i * N
  return last

freader = open("A-large.in", "r")
fwriter = open("output.out", "w")

t = freader.readline()

for i in range(1, int(t) + 1):
  t = freader.readline()
  if(int(t) == 0):
    fwriter.write("Case #{}: {}\n".format(i, "INSOMNIA"))

  else:
    fwriter.write("Case #{}: {}\n".format(i, Bleatrix(int(t))))

fwriter.close()
freader.close()