import sys
def solve(x,n):
    val = n
    if n == 0 :
        print "Case #%s: INSOMNIA" %(x)
        return
    flag = []
    for i in range(0,10):
        flag.append(False)
    while True :
                  #print n
                  tmp = n
                  while tmp > 0 :
                      flag[tmp%10] = True
                      tmp /= 10
                  #flag[tmp%10] = True
                  again = False
                  for i in range(0,10):
                      if flag[i] == False :
                          again = True
                          break
                  if again == False :
                      break
                  n += val
    print "Case #%s: %s" %(x,n)
t = int(raw_input())
x = 1
for i in range(0,t):
        n = int(raw_input())
        solve(x,n)
        x = x+1
