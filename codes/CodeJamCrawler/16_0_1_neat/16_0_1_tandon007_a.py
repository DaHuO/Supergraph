def fun(n):
          i = 1
          l= ['0','1','2','3','4','5','6','7','8','9']
          ans = n*i # calculate answer
          fl = list(str(ans))
          if ans == 0:return "INSOMNIA"
          else:
               c = 0
               while(c<10):
                          if(l[c] in fl):
                                        c = c+1
                          else:
                              i = i+1
                              ans = n*i
                              nl = list(str(ans)) #convert ans to str and to list
                              fl = fl+nl  # new list
               return ans

t = int(raw_input())
for st in range(t):
                  n = int(raw_input())
                  print 'Case #' + str(st+1) + ': ' + str(fun(n))
