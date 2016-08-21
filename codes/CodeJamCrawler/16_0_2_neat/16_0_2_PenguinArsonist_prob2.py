import fileinput
target = open("C:\Users\Penguin\Desktop\Jam\out",'w')

def flip(string):
  string = string.strip()
  out = 0
  count = len(string)-1

  if string[-1] =='-':
    out += 1

  while count > 0:
    if string[count] != string[count-1]:
      out += 1
    count -= 1

  return str(out)

case = 0

for line in fileinput.input():
  
  if not fileinput.isfirstline():
    case += 1
    target.write("Case #"+str(case)+": "+flip(line)+'\n')



