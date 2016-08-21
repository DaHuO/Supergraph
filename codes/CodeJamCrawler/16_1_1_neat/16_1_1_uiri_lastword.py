import sys, math

stdin = sys.stdin.readlines()
cases = int(stdin.pop(0))
for case in xrange(cases):
    word = stdin.pop(0).strip()
    answer = ""
    for letter in word:
        if len(answer) == 0:
            answer = letter
            continue
        if letter >= answer[0]:
            answer = letter + answer
        else:
            answer = answer + letter
    print "Case #" + str(case+1) + ": " + answer
