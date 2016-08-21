class Solution:
    def process(self, cakes, case):
        num = len(cakes)
        if num == 0:
            print "Case #%d: 0" % case
            return
        if num == 1:
            if cakes[0] == True:
                print "Case #%d: 0" % case
                return
            elif cakes[0] == False:
                print "Case #%d: 1" % case
                return

        ans = 0
        i = 1
        while i < num:
            if cakes[i-1] == False and cakes[i] == True:
                ans += 1
            if cakes[i-1] == True and cakes[i] == False:
                ans += 1
            i += 1

        if cakes[num-1] == False:
            ans += 1
        print "Case #%d: %d" % (case, ans)

def pancake_to_binary(pancake):
    if pancake == '+':
        return True
    elif pancake == '-':
        return False

T = int(raw_input())
for i in xrange(T):
    line = raw_input()
    cakes = map(pancake_to_binary, list(line))

    s = Solution()
    s.process(cakes, i + 1)
