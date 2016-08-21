digit = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def isInString( s, lookfor ):
    for c in lookfor:
        if c in s :
            s = s.replace(c,"",1)
        else:
            return False,s
    return True,s

def decode( s, current, out ):
    #print "decode", s, current, out
    if len(s) == 0 :
        return out
    else:
        # remove "current letter from string"
        # check first if we have all those letter
        isIn , newS = isInString(s, digit[current])
        #print isIn , newS
        if isIn == True :
            # search further
            for i in range(current,10) :
                #print "in i" , i
                ret = decode(newS, i, out+str(current))
                if ret != None:
                    return ret
        else:
            # search further
            for i in range(current+1,10) :
                #print "out i" , i
                ret = decode(s, i, out)
                if ret != None:
                    return ret
            

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s = raw_input()
  k = decode( s, 0, "" )
  print "Case #{}: {}".format(i, k)

  # check out .format's specification for more formatting options
