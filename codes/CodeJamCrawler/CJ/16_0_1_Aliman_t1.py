with open("t1.in") as f:
	content = f.readlines()

case = 0
for strNum in content[1:]:
    case += 1
    N = int(strNum)

    if N == 0:
        print("Case #"+str(case)+": INSOMNIA")
        continue

    # Index represents digit and value if seen
    seen = [False]*10

    # When all numbers detected, this variable will be 0
    finished = 10

    step = N
    N = 0

    while finished > 0:
        N += step 
        strN = str(N)
        for c in strN:
            digit = int(c)
            if not seen[digit]:
                finished -= 1
                seen[digit] = True
            
    print("Case #"+str(case)+": "+str(N))
