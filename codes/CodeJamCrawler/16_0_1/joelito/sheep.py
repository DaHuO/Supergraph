#imports

def seenAll(arr):
 for i in range(10):
  if (arr[i] == False):
   return False
 return True
 

def bleatrix(arr, numb):
 for ch in str(numb):
  arr[int(ch)] = True
 return arr

 
f = open("A-large.in")

T = int(f.readline())
counter = 1

while counter <= T:
 c = int(f.readline())
 if c == 0:
  print ("Case #" + str(counter) + ": INSOMNIA")
  counter += 1
 else:
  arr = [False]*10
  i = 1
  arr = bleatrix(arr,c)
  while (not seenAll(arr)):
    arr = bleatrix(arr,int(c)*i)
    i += 1
  i = i-1
  print ("Case #" + str(counter) + ": " + str(i*(int(c))))
  counter += 1

 
 

 


  