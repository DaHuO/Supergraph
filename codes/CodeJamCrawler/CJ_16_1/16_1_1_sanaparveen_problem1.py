import string
def Last_Word(S, Len):

    if len >= 1:
        reslist = [S[0]]
    for x in S[1:]:
        Vlist = []
        for y in reslist:
            Vlist.append( x+y);
            Vlist.append( y+x );
        reslist = sorted(Vlist)
    x = reslist[len(reslist)-1]
    while Len != 0:
      index = 1
      if x in string.ascii_uppercase:
          Result = reslist[len(reslist)-1]
          return Result
          break
      elif Len >= 1:
          x = x[index:]
          index += 1
          Len -= 1



T = int(input()) #take Number of testcase

if T>=1 and T<=100: #Test Case Validity
   for x in range(1, T+1):
       S = raw_input()
       slen = len(S)
       if slen >= 1 and slen <= 15:
          res = Last_Word(S, slen)
          print "Case #{}: {}".format(x, res)











