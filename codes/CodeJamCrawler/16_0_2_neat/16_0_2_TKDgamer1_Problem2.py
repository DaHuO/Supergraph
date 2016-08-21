input = open("B-large.in","r")
output = open("output.txt","w")

for x in range(int(input.next())):
   stack = input.next()
   counter = 0
   while("-" in stack):
      index = stack.rfind("-")
      temp = stack[index+1:len(stack)]
      for y in range(index,-1,-1):
         if(stack[y] == "-"):
            temp = "+" + temp
         else:
            temp = "-" + temp
      stack = temp
      counter += 1
   output.write("Case #"+str(x+1)+": "+str(counter)+"\n")