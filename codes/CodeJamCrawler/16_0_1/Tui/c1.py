f = open('c1.in', 'r')
fclear = open('c1.out', 'w')
fclear.write("")
fclear.close()

fw = open('c1.out', 'a')

n = int(f.readline())
c = 1
for x in range(0, n):
  m = int(f.readline())
  num = m
  temp = str(m)
  count = 2
  while True: 
    num = m*count
    temp += str(num)
    if num == 0:
      break
    count = count + 1
    if "1" not in temp:
      continue
    elif "2" not in temp:
      continue
    elif "3" not in temp:
      continue
    elif "4" not in temp:
      continue
    elif "5" not in temp:
      continue
    elif "6" not in temp:
      continue
    elif "7" not in temp:
      continue
    elif "8" not in temp:
      continue
    elif "9" not in temp:
      continue
    elif "0" not in temp:
      continue
    else:
      break

  if num == 0:
    fw.write("Case #" + str(c) + ": INSOMNIA \n")
  else:
    fw.write("Case #" + str(c) + ": " + str(num) + "\n")

  c = c +1
