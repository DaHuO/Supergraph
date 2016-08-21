infile = open("A-large.in", "r")
outfile = open("A-large.out", "w")


T = int(infile.readline())

N = []

for case in range(T):
    N.append(str(infile.readline()))

for case in range(T):
    Seen = [1,0,0,0,0,0,0,0,0,0]
    coefficient = 0
    if(int(N[case]) == 0):
        N[case] = "INSOMNIA"
        continue;
    while(Seen != [0,1,2,3,4,5,6,7,8,9]):
        coefficient += 1
        for digit in str(int(N[case]) * coefficient) :
            Seen[int(digit)] = int(digit)
    N[case] = str(int(N[case]) * coefficient) 
        

for case in range(T):
    outfile.write("Case #" +str(case + 1) + ": " + N[case] +"\n")

infile.close()
outfile.close()
