class Solution(object):
    def getLastWord(self, word):
        curMax = 0
        result = []
        wordList = list(word)
        for i in range(len(wordList)):
            if len(result) == 0:
                result.append(wordList[i])
                curMax = ord(wordList[i])
                continue
            else:
                if ord(wordList[i]) >= curMax:
                    result.insert(0, wordList[i])
                    curMax = ord(wordList[i])
                else:
                    result.append(wordList[i])

        return ''.join(result)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
test = Solution()

for i in range(1, t + 1):
    word = input()
    print("Case #{}: {}".format(i, test.getLastWord(word)))
    # check out .format's specification for more formatting options
