def findFirstDivisor(n):
    for i in range(2, min(1+(n**0.5),10000)):
        if n%i==0:
            return i
    return None
    
def valid(n):
    result = []
    for i in range(2,11):
        d = findFirstDivisor(int(n, i))
        if d==None:
            return None
        result.append(d)
    return result

N = 30
J = 500
count = 0
for i in range(2**N):
    n = "1"+"{{:0>{}}}".format(N).format(bin(i)[2:])+"1"
    res = valid(n)
    if res!=None:
        print(n, ' '.join([str(i) for i in res]), flush=True)
        count += 1
    if count==J:
        break


# filename = "p3example.in"
# f = open(filename,"r")
# N = int(f.readline())
# for i in range(N):
#     print("Case #{}:".format(i+1), solve(preprocess(f.readline())))
# f.close()
