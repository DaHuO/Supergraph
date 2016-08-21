from sys import stdin

def printAnswer(caseIndex, answer):
    print("Case #", caseIndex+1, ": ", answer, sep='')

T = int(input())
for t in range(T):
    n = int(input())
    if n == 0:
        printAnswer(t, 'INSOMNIA')
    else:
        seen = 0
        numbers = {str(i): False for i in range(10)}
        i = 1
        while seen < 10:
            for c in str(n * i):
                if not numbers[c]:
                    numbers[c] = True
                    seen += 1
            i += 1
        printAnswer(t, n * (i - 1))
