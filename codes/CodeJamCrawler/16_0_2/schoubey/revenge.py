import sys
std_in = sys.stdin

T = int(std_in.readline())

for i in range(T):
    input = std_in.readline()
    count = 0
    flag1 = 0
    flag0 = 0
    for j in range(len(input)):
        if input[j] == '-':
            if flag0 != 1:
                count = count + 1
                flag0 = 1
                if flag1 == 1:
                    count = count + 1
                    flag1 = 0
        elif input[j] == '+':
            flag1 = 1
            if flag0 == 1:
                flag0 = 0
    print("Case #" + str(i+1) + ": " + str(count))