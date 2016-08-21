def test_case(x):
    if(int(x) == 0):
        return "INSOMNIA"
    else:
        mult = 1
        numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]
        zero = True
        while(zero):
            snum = str(int(x)*mult)
            for y in range(0, len(snum)):
                numbers[int(snum[y])]+=1
            zeroes = 10
            for y in range(0, len(numbers)):
                if(numbers[y] != 0):
                    zeroes-=1
                if(zeroes == 0):
                    zero = False
            if(zero):
                mult+=1
        return int(x)*mult
file_in = open(r"C:\Users\Isaac\Desktop\A-large.in")
file_out = open(r"C:\Users\Isaac\Desktop\qr1testlarge.txt", mode="w")
numcases = file_in.readline()
cases = []

for x in range(0, int(numcases)):
    cases.append(file_in.readline())
    cases[x] = cases[x][0: len(cases[x])-1]
for x in range(0, len(cases)):
    file_out.write("Case #" + str(x+1) + ": " + str(test_case(cases[x]))+ "\n")
file_in.close()
file_out.close()