def checkSleep(N, Base,count):
    for x in range(2, 101):
        for y in str(N*x):
            if y not in Base:
                Base += y
                count += 1
        if count == 10:
                return N*x
    return

def countsheep(N):

    stringBase = ""
    count = 0
    for x in str(N):
        if x not in stringBase:
            stringBase += x
            count += 1
    if count == 10:
        return N
    sleep = checkSleep(N, stringBase,count)
    return sleep

T = int(input()) #take Number of testcase

if T>=1 and T<=100: #Test Case Validity
   for x in range(1, T+1):
       N = int(input())
       if N >= 0 and N <= 1000000:
          res = countsheep(N)
          if res == None:
              print "Case #{}: INSOMNIA".format(x)

          else:
              print "Case #{}: {}".format(x, res)
