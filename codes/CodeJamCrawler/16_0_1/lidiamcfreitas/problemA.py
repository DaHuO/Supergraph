# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer

objective = set([0,1,2,3,4,5,6,7,8,9])
dictionary_memoize = {}


for i in range(1,1000001): # 1000001
    res = i
    set_result = set()
    while(set_result != objective):
        set_result = set_result.union(set([int(x) for x in str(res)]))
        res += i
    dictionary_memoize[i] = res - i

for i in range(1, t + 1):
    n = int(input())  # read a list of integers, 2 in this case
    if n == 0:
        print("Case #{}: {}".format(i, "INSOMNIA"))
    else:
        result = dictionary_memoize[n]
        print("Case #{}: {}".format(i, result))
    # check out .format's specification for more formatting options
    
