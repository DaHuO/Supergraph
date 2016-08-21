import sys

n = (int) (sys.stdin.readline().strip())
for i in range (1, n+1):
    word = sys.stdin.readline().strip()
    answer = word[0]
    for c in word[1:]:
        if ord(c) >= ord(answer[0]):
            answer = c + answer
        else:
            answer = answer + c
    print("Case #{}: {}".format(i, answer))
