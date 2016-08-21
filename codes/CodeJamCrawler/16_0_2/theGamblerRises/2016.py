__author__ = 'gambler'
class Solution:

    def pancakes(self, A):
        l = len(A)
        flip = False
        attempts = 0
        for i in xrange(l-1, -1, -1):
            val = 0 if A[i]=='-' else 1
            x = val^1 if flip else val
            if x==0:
                attempts += 1
                flip = not flip
        return attempts

#fin = open("/Users/gambler/Documents/pycharm/input.txt", "r")
fin = open("/Users/gambler/Documents/pycharm/B-large.in", "r")
fout = open("/Users/gambler/Documents/pycharm/output.txt", "w")
cases = int(fin.readline().strip())
s = Solution()
for case in range(cases):
    val = s.pancakes(fin.readline())
    fout.write("Case #"+str(case+1)+": "+str(val)+"\n")

fin.close()
fout.close()