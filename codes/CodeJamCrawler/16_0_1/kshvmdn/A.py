class Solution(object):
    def fallAsleep(self, n):
        if n == 0:
            return "INSOMNIA"

        step = 0
        # test if 1023, then stop
        bitsTable = 0

        while bitsTable != 1023:
            step += 1

            numBits = 0
            numString = str(n * step)

            for i in numString:
                numBits |= 1 << int(i)

            bitsTable |= numBits

        return n * step

t = int(input())
test = Solution()

for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {}".format(i, test.fallAsleep(n)))
