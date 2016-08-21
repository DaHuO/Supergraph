a = '10000000000000000000000000000001'
div = '11'
ans = set()

def check(b, div, shift):
    for i in range(len(div)):
        if (b[shift + i] == '1' and div[i] == '1'):
            return False 
    return True 

def put(b, div, shift):
    u = b[:shift]
    for i in range(len(div)):
        if div[i] == '1' or b[shift + i] == '1':
            u += '1'
        else:
            u += '0'
    u += b[-( len(b) - len(div) - shift  ):]
    return u

def recur(b, div):
    
    ans.add(b)
    if len(ans) > 500:
       return 
    for i in range(len(b) - len(div)):
        if check(b, div, i):
            merge = put(b, div, i)
            recur(merge, div)



def k(a, div):
    l = len(div)
    b = div + a[l:-l] + div
    recur(b, div)



k(a, div)
print 'Case #1:'
# print len(ans)
for a in list(ans)[:500]:
    print a,3,4,5,6,7,8,9,10,11
    # for base in range(2, 11):
    #     v = int(a, base)
    #     print v, v % (base + 1)

