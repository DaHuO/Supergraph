T = int(input())
for t in range(T):
    N = int(input())
    if N == 0:
        print("Case #%d:" % (t+1), "INSOMNIA")
        continue
    digits = set(list(str(N)))
    total = N
    while len(digits) != 10:
        total += N
        digits |= set(list(str(total)))
        #print(digits, total)
    print("Case #%d:" % (t+1), total)
    

    
        
