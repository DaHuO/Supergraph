fin = open('A.in', 'r')
fout = open('file.out', 'w')
n = fin.readline()
nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
values = []
def getarr(s):
    letters = [0 for i in range(26)]
    for c in s:
        letters[ord(c)-65] += 1
    return letters
    
def dif(a,b):
    out = []
    for i in range(len(a)):
        out.append(a[i]-b[i])
    return out
def addition(a,b):
    out = []
    for i in range(len(a)):
        out.append(a[i] + b[i])
    return out

def dp(cur,vals):
    #print cur,vals
    if min(vals) < 0:
        return ''
    if sum(vals) == 0:
        #print cur
        return str(cur)
    if cur > 9:
        return ''
    t = ''
    if min(dif(vals,values[cur])) >= 0:
        t = dp(cur,dif(vals,values[cur]))
        if t != '':
            #print cur,t
            #print cur,str(cur) + t
            return str(cur) + t
    i= cur+1
    while i <= 9:
        if min(dif(vals,values[i])) >= 0:
            t = dp(i,dif(vals,values[i]))
            t = dp(i,dif(vals,values[i]))
            if t != '':
                #print cur,str(cur)+t
                return str(cur) + t
        i+=1
    return t
        
        
for l in range(int(n)):
    chars = fin.readline().strip()
    out = ''
    vals = getarr(chars)
    for i,num in enumerate(nums):
        values.append(getarr(num))
        """cur = getarr(num)
        while min(dif(vals,cur)) >= 0:
            out += str(i)
            vals = dif(vals,cur)"""
    out = dp(0,vals)[1:]
    test = [0 for i in range(26)]
    for c in out:
        test = addition(test,values[int(c)])
    if sum(dif(vals,test)) > 0:
        print chars,out
    #if len(out) == 0:
    #print chars, out
    fout.write("Case #%d: %s\n"%(l+1,out))
        
    
fin.close()
fout.close()
