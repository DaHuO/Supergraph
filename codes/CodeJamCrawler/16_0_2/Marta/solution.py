T = input()
for i in range(T):
    S = raw_input()

    # Solution: count number of sign changes, +1 if bottom of stack is -
    S += '+'
    count = 0
    for j in range(len(S)-1):
        count += 0 if S[j] == S[j+1] else 1
    sol = str(count)
    print 'Case #'+str(i+1)+": " + sol
