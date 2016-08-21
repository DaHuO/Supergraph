import sys

def flip_pancakes(stack):
    lstack = list(stack)
    lstack.reverse()
    #print lstack
    
    count = 0
    while True:
        #find the first "-"
        try:
            first_sad = lstack.index("-")

            lstack = lstack[first_sad:] #need to keep it there

            count_sad = lstack.count("-")
            count_happy = lstack.count("+")
            #print count_sad, count_happy
            if count_sad >= count_happy: #if more sads, change sads to happy
                lstack = [help(sign) for sign in lstack]
                
                count+= 1
            else:#more happys, change happys to sads
                lstack = [help(sign) for sign in lstack]
                
                count+= 1
            
            
        except ValueError:
            return count
            break
            
def help(sign):
    if sign == '+':
        return '-'
    elif sign == '-':
        return '+'
    
infile = sys.stdin
next(infile)
count = 1
for line in infile:
    if not line:
        break
    
    nice_line = line.rstrip()
    print "Case #" + str(count) + ": " + str(flip_pancakes(nice_line))
    count += 1
    