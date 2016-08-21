class Solution(object):
    def getMissing(self, N, list):
        result = []
        dict = {}
        for i in range(len(list)):
            for j in range(len(list[i])):
                if list[i][j] in dict:
                    del dict[list[i][j]]
                else:
                    dict[list[i][j]] = True

        for key, value in dict.items():
            result.append(key)

        result.sort()

        return ' '.join("{0}".format(n) for n in result)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
test = Solution()

for i in range(1, t + 1):
    N = int(input())
    list = []

    for j in range(2 * N - 1):
        list.append([int(k) for k in (input().split(' '))])

    print("Case #{}: {}".format(i, test.getMissing(N, list)))
    # check out .format's specification for more formatting options
