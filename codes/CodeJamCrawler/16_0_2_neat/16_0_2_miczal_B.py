T = int(input())
for t in range(T):
    S = input()
    changes = 0
    for i in range(len(S)):
        if i == len(S) - 1:
            if S[i] == '-':
                changes+=1
        elif S[i+1] != S[i]:
            changes+=1
    print("Case #" + str(t+1) + ": " + str(changes))

