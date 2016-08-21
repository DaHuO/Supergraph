__author__ = 'Nikhil'

t = int(input())  # read a line with a single integer
for testCase in range(1, t + 1):
    inputForTestCase = input()
    myword = inputForTestCase[0];
    for s in range(1, len(inputForTestCase)):
        if myword[0] > inputForTestCase[s]:
            myword = myword + inputForTestCase[s]
        else:
            myword = inputForTestCase[s] + myword

    print("Case #{}: {}".format(testCase, myword))