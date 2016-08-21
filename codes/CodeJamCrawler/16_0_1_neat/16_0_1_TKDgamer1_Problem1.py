input = open("A-large.in", "r")
output = open("output.txt","w")
for x in range(int(input.next())):
   n = int(input.next())
   if(n == 0): 
      output.write("Case #" + str(x+1) + ": INSOMNIA\n")
   else:
      b1=b2=b3=b4=b5=b6=b7=b8=b9=b0=False
      counter = 1
      sheep = ""
      while(not(b1 and b2 and b3 and b4 and b5 and b6 and b7 and b8 and b9 and b0)):
         sheep = str(counter*n)
         for y in sheep:
            if(y == "1"):
               b1 = True
            elif(y == "2"):
               b2 = True
            elif(y == "3"):
               b3 = True
            elif(y == "4"):
               b4 = True
            elif(y == "5"):
               b5 = True
            elif(y == "6"):
               b6 = True
            elif(y == "7"):
               b7 = True
            elif(y == "8"):
               b8 = True
            elif(y == "9"):
               b9 = True
            elif(y == "0"):
               b0 = True
         counter += 1
      output.write("Case #" + str(x+1) + ": " + str(n*(counter-1))+"\n")