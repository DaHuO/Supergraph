f = open('c2.in', 'r')

# Clear Output
fclear = open('c2.out', 'w')
fclear.write("")
fclear.close()

fw = open('c2.out', 'a')

n = int(f.readline())
c = 1
for x in range(0, n):
  m = list(f.readline())
  s = []
  last_minus = -1
  for idx,item in enumerate(m):
    if item == "-":
      last_minus = idx
    s.append(item)

  is_minus = False
  count = 0
  while True:
    temp = []
    temp_lm = last_minus
    is_minus = False
    if last_minus >= 0:
      count = count + 1

      for idx,item in enumerate(list(s[0:last_minus])):
        if item == "+":
          last_minus = idx
          is_minus = True
          temp.append("-")
        if item == "-":
          temp.append("+")

      s[0:temp_lm] = temp
      s[temp_lm] = "+"

      if is_minus == False:
        last_minus = -1
        break;
      
    else:
      break;

  fw.write("Case #" + str(c) + ": " + str(count) + " \n")
  c = c +1