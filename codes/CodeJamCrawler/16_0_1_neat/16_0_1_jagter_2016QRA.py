import sys

ind = open("A-large.in", "r")
outd = open("A-large.out", "w")

T = int(ind.readline())

for i in range(1, T+1):
    N = int(ind.readline().strip())
    N_ = N
    digits = set()
    count = 0
    
    result = ""
    solved = False
    
    if N == 0:
        result = "INSOMNIA"    
    else:
        while solved == False:
            count += 1
            N_ = count * N
            number = str(N_)
            for d in number:
                while not d in digits:
                    digits.add(d)
                if len(digits) >= 10:
                    solved = True
                    result = str(N_)
    
    print("Case #"+str(i)+": "+result+"\n")
    outd.write("Case #"+str(i)+": "+result+"\n")

ind.close()
outd.close()

