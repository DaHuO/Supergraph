# Daniele Perazzolo April 2016
# Code Jam 2016

def problem(num):
    if num == 0:
        return "INSOMNIA"
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0.0
    while len(digits) != 0:
        count += num
        tempStr = str(count).split(".")
        for char in range(0, len(tempStr[0])):
            # print("{}".format(tempStr[0][char]))
            if int(tempStr[0][char]) in digits:
                digits.remove(int(tempStr[0][char]))

    output = str(count).split(".")
    return output[0]

t = int(input()) #Case number
for i in range(1, t + 1):
    n = float(input())
    print("Case #{}: {}".format(i, problem(n)))