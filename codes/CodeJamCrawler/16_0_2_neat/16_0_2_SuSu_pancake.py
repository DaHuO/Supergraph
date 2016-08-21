def pancake(x):
  inp = list(x)
  count = 0
  N = len(inp)-1

  for i in range(N):
    if N == 0 :
      if inp[i] == "-":
        count = 1
      else:
        count = 0
    if (inp[i] == "+" and inp[i+1] == "-"):  
      inp[i] == "-"
      count +=1
    if (inp[i] == "-" and inp[i+1] == "+"): 
      inp[i] == "+"
      count +=1
  if(inp[-1] == "-"):
    count += 1          
  return count


file = open("B-large.in",'r')
l = int(file.readline())
temp =  file.read().splitlines()
for i in range (l):
    print("CASE #"+ str(i+1) +': '+ str(pancake(temp[i])))

  
  


    
    

  
  

  
    
    
  
  
