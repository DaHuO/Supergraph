import random
# Given a number, keep mutiplying by the next number in the table till you see all the digits in its product.



def findSleepNumber(x):
        if x == 0:
                return("INSOMNIA")
        allDigits = set(['1','2','3','4','5','6','7','8','9','0'])
        seenDigits = set()
        i = 0
        while True:
                i = i + 1
                checkNum = x * i
                nums = set(list(str(checkNum)))
                seenDigits = seenDigits.union(nums)
                if len(seenDigits) == 10:
                        return checkNum

def test():
        while(True):
                print(findSleepNumber(int(raw_input("Enter a number: "))))

def gTest():
        for i in range(100):
                print(findSleepNumber(random.randint(999999, 1000000)))

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
        n = int(raw_input())  # read a list of integers, 2 in this case
        print "Case #{}: {}".format(i, findSleepNumber(n))
