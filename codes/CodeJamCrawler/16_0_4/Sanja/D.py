t = int(input())

for BULLSHIT in range(t) :
  s = input().split()
  
  k = int ( s[2] ) 
  temp = "Case #" + str(BULLSHIT+1) + ": "
  while k :
    temp += str(k) + " "
    k -= 1
  print (  temp )
  