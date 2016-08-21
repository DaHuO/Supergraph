T = int(input())  # read a line with a single integer
# n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

def hasADigit(string, digit):
    for c in digit:
        i = string.find(c)
        if i == -1:
            return False
        string = string[:i] + string[i + 1:]
    return True

def rmInString(string, digit):
    for c in digit:
        i = string.find(c)
        string = string[:i] + string[i + 1:]
    return string


numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"];
answer = []

def check(string, num_index):
    global numbers
    global answer
    while hasADigit(string, numbers[num_index]):
        answer.append(num_index);
        string = rmInString(string, numbers[num_index])
    if not string:
        return True

    if num_index != 9:
        if not check(string, num_index + 1):
            if answer == []:
                return False
        else:
            return True
        while answer != [] and answer[-1] == num_index:
            string = string + numbers[answer.pop()]
            if check(string, num_index + 1):
                return True
        return False
    else:
        while answer != [] and answer[-1] == 9:
            answer.pop()
        return False


for case in range(1, T + 1):
        print("Case #{}: ".format(case), end="")
        string = input()
        check(string, 0)
        for d in answer:
            print("{}".format(d), end="")
        print("")
        answer = []
