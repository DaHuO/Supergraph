cases = int(input())

for x in range(int(cases)):

    N = int(input())
    if N == 0:
        print("Case #" + str(x+1) + ": INSOMNIA")
        continue
        
    out = []
    i = 1

    last_number = 0

    while(len(out) < 10):
        A = N * i
        last_number = A
        A = list(str(A))
        for r in range(len(A)):
            if A[r] not in out:
                out.append(A[r])	
        i += 1
        
            
    print("Case #" + str(x+1) + ": " + str(last_number))
