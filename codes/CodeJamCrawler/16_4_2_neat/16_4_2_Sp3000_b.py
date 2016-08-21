import itertools

'''
def f2(L):
    total = 0

    for a in itertools.product(range(2), repeat=len(L)):
        p = 1

        for x,y in zip(L, a):
            p *= x if y else 1-x

        total += p*(a.count(0) == a.count(1))

    return total
'''

def f(L, a=0, b=0):
    if a > b+len(L):
        return 0
    if b > a+len(L):
        return 0

    if len(L) == 0:
        return (a==b)

    return L[0]*f(L[1:],a+1,b) + (1-L[0])*f(L[1:],a,b+1)

def g(L, b):
    best = 0
    best_item = None
    
    for x in itertools.combinations(L, b):
        best = max(best, f(x))
        best_item = x

    return best, x

with open("B-small-attempt3.in") as infile:
    with open("b.out", "w") as outfile:
        cases = int(next(infile))

        for case in range(1, cases+1):
            a, b = list(map(int, next(infile).split()))
            nums = list(map(float, next(infile).split()))
            nums.sort()

            best = 0
            best_x = None

            for i in range(b+1):
                x = nums[:i] + nums[-(b-i):] if i < b else nums[:b]
                score = f(x)

                if score > best:
                    best = score
                    best_x = x

            '''
            p, q = g(nums, b)

            if best != p:
                print(nums, b, best, best_x, x, score, p, q)
            '''

            print("Case #{}: {:.10f}".format(case, best), file=outfile)
       
