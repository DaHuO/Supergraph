
import string
Validate_S = (string.printable).replace('+,-',"")

def Happy_pancake():
    global S
    global final_count
    if S[0] == '+':
        first_positive = 1
        first_negative = 0
        onneg = 0
        pointneg = 0
    else:
        first_negative = 1
        first_positive = 0
        onpos = 0
    count = 0
    if first_positive == 1:
        for x in S:
            if onneg == 0 and x == '-':
                onneg = 1
                pointneg = count
            if onneg == 1 and (x == '+' or slen == count+1):
                S = S[:pointneg].replace('+','-')+S[pointneg:slen]
                final_count += 1
                return 1
            count = count+1
        if onneg == 0:
            return 0
    elif first_negative == 1:
        for x in S:
           if onpos == 0 and x == '+':
               onpos = 1
               pointpos = count
           if onpos == 1 and (x == '+' or slen == count+1):
               S = S[:pointpos].replace('-','+')+S[pointpos:slen]
               final_count += 1
               return 1
           count = count+1

        if onpos == 0:
            S = S.replace("-","+")
            final_count += 1
            return 1
    return 0
    pass

def Revenge_Pancake(slen):
    Flag = 1
    while (Flag != 0):
        Flag = Happy_pancake()
    pass
T = int(input()) #take Number of testcase

if T>=1 and T<=100: #Test Case Validity
   for x in range(1, T+1):
       S = raw_input()
       slen = len(S)
       Scorrect = True
       for y in S:
           if y in Validate_S:
              Scorrect = False
              break
       if slen >= 1 and slen <= 100 and Scorrect == True :
          final_count = 0
          Revenge_Pancake(slen)
          print "Case #{}: {}".format(x, final_count)











