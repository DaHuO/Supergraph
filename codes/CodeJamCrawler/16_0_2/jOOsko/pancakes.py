import sys

N = int(sys.stdin.readline())

def count(pancakes):
    pancakes = [[-1,1][j == "+"] for j in reversed(pancakes)]
    correct = 1
    times = 0
    for p in pancakes:
        if correct:
            if p == -1: ## flip
                times += 1
                correct = 0
        else:
            if p == 1:
                times += 1
                correct = 1
    return times

for case in range(N):
    pan = sys.stdin.readline().strip()
    print("Case #" + str(case + 1) + ":", count(pan))  
