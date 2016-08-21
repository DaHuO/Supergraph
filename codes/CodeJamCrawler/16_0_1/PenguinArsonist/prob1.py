import fileinput
win = set(['1','2','3','4','5','6','7','8','9','0'])
target = open("C:\Users\Penguin\Desktop\Jam\out",'w')
case = 0
for line in fileinput.input():

  if not fileinput.isfirstline():
    case += 1
    mult = int(line)
    if mult == 0:
      target.write("Case #"+str(case)+": INSOMNIA\n")
      continue
    temp = set()  
    count = 0  
    while temp != win:
      count +=1
      temp |= set(list(str(count*mult)))
    target.write("Case #"+str(case)+": "+str(count*mult)+"\n")
