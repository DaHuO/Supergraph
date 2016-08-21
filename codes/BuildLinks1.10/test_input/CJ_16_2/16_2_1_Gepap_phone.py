numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
           "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


def findnumber(case, result):
    for number in numbers:
        for char in number:
            if char not in case:
                break
        else:
            temp = case
            for char in number:
                temp = temp.replace(char, "", 1)
            tempresult = result + str(numbers.index(number))
            if temp == '\n' or not temp:
                return tempresult
            a = findnumber(temp, tempresult)
            if a:
                return a


with open('input.txt') as infile:
    lines = infile.readlines()
    T = int(lines[0])
    cases = lines[1:]

with open('output.txt', 'w') as outfile:
    for index, case in enumerate(cases):
        # print findnumber(case, "")
        outfile.write("Case #%d: %s\n" % (index + 1, findnumber(case, "")))
