def findval(N):
    if N==0:
        return "INSOMNIA"
    numbers=[0]*10
    found = False

    multiplier=1
    while(found == False):
        current = list(str(N*multiplier))
        for item in current:
            if numbers[int(item)] == 0:
                numbers[int(item)] = multiplier

        if 0 not in numbers:
            found = True
            return max(numbers) * N

        multiplier = multiplier + 1

f = open("dataset.txt", "r")
o = open("output.txt", "w")

numberOfCases = int(f.readline())

for item in range(0,numberOfCases):
    current = int(f.readline())
    string = "Case #{}: ".format(item + 1), "{}\n".format(findval(current))
    o.writelines(string)

