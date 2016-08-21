import sys
#sys.stdin = open("input.txt","r")
fout= open("output.txt","w")

numbers =  ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")

ans = ""
def is_in(number,t) :
    #print(1,t)
    s = [x for x in t]
    for c in number :
        if c in s :
            s.remove(c)
        else :
            return 0
    return 1

def get(number,t) :
    #print(2,t)
    s = [x for x in t]
    for c in number :
            s.remove(c)
    return s

def is_number(s,total) :
    global ans
    #print(s)
    if len(s)==0 :
        ans = total
        return 1
    i = 0
    for number in numbers :
        if is_in(number,s):
            if is_number(get(number,s),total+str(i)) :
                return 1
        i+=1
    return 0

tests = int(input())
test = 1
while test<=tests :
    s = list(input())
    is_number(s,"")

    k = 0
    
    
    fout.write("Case #%s: %s\n"%(test,ans))
    test+=1
fout.close()
