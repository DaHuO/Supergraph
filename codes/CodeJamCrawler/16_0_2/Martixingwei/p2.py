
def preprocess(i):
    i = i.strip()
    import re
    i = re.sub("-+", "-", i)
    i = re.sub("\++", "+", i)
    return i

def solve(i):
    if i=="+":
        return 0
    if i=="-":
        return 1
    if i[-1]=="-":
        return solve(i[:-1])+2
    if i[-1]=="+":
        return solve(i[:-1])
    
filename = "B-large.in"
f = open(filename,"r")
N = int(f.readline())
for i in range(N):
    print("Case #{}:".format(i+1), solve(preprocess(f.readline())))
f.close()
