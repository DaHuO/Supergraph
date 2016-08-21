def flipPancake(S):
    cnt = 0
    side = S[0]
    
    for idx in range(1,len(S)):
        if S[idx] != side:
            cnt += 1
            side = S[idx]
            
    if S[len(S)-1] == '-':
        cnt += 1
    
    print("Case #" + str(i) + ": " + str(cnt))
    
t = int(input())
for i in range(1, t + 1):
    S = input()
    flipPancake(S)