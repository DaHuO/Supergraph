strs = 'ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE'.split()
'''     Z         W                    X         G       '''
'''                   H                  S               '''
'''                           R                          '''
'''          O                  F                        '''
'''                                                  N   '''


order = [0, 2, 6, 8, 3, 7, 4, 1, 5, 9]



def make_bag(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    return d

num_bags = map(make_bag, strs)

def intersects(small, big):
    for c in small:
        if c not in big or small[c] > big[c]:
            return False
    return True


def rem(small, big):
    for c in small:
        if c in big:
            big[c] -= small[c]
            if big[c] == 0:
                del big[c]

    
def solve(s):
    bag = make_bag(s)

    nums = [0 for i in xrange(10)]

    for u in order:
        while intersects(num_bags[u], bag):
            nums[u] += 1
            rem(num_bags[u], bag)
    ans = ''
    for i in xrange(len(nums)):
        for j in xrange(nums[i]):
            ans += str(i)
    return ans


t = int(raw_input())
for tt in xrange(t):
    s = raw_input()
    print 'Case #{}: {}'.format(tt+1, solve(s))
