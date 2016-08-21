t = int(input())
result = []
for i in range(1, t + 1):
    k, c, s = [int(x) for x in input().split(" ")]  # read a list of integers, 2 in this case
    result = []
    toSum = k**(c-1)
    
    for j in range(s):
        result += [1 + j*toSum]
    
    print("Case #{}: {}".format(i, " ".join([str(x) for x in result])))
        