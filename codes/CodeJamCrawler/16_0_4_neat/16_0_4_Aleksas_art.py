# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    K,C,S = input().split(" ")
    print("Case #{}: {}".format(i, ' '.join(map(str,[j for j in range(1,int(K)+1)]))))
