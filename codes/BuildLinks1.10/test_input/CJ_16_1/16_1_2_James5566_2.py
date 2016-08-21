# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
    N=int(input())*2 - 1
  # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    result_list=[]
    result=[]
    for i in range(N):
        result_list.extend([int(s) for s in input().split(" ")])
    
    # print(result_list)
    counts = dict()    
    for i in result_list:
        counts[i] = counts.get(i, 0) + 1
    # print(counts)
    for item in counts.keys():
        if counts[item]%2==1:
            result.append(item)
    result.sort()
    result = [str(num) for num in result]
    print("Case #{}: {}".format(j, " ".join(result)))
  # check out .format's specification for more formatting options