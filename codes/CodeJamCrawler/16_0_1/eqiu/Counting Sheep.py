# ECOO 2016 Round 1
# Problem 
# Eric Qiu, Moeyyad Qureshi, Nick Robinson, Simeng Yang

f = open("A-large.in", "r")
output = open("OUTPUT.txt", "w")

numCases = int(f.readline().strip())

for case in range(1, numCases + 1):
    N = int(f.readline().strip())
    if N == 0:
        output.write("case #" + str(case) + ": INSOMNIA\n")
    else:
        digitCount = [0] * 10
        for i in range(N, 9999999, N):
            stringI = str(i)
            for j in range(10):
                if str(j) in stringI:
                    digitCount[j] += 1
            if 0 not in digitCount:
                output.write("case #" + str(case) + ": " + stringI + "\n")
                break

f.close()
output.close()