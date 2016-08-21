"""
Created on Apr 8, 2016

@author: K.Yao
"""


def flip_plus(stack):
    print(stack)
    top_count = 0
    for i in range(-1, -(len(stack)), -1):
        if stack[i] == "-":
            break
        top_count += 1
    temp_list = []
    for null in range(top_count):
        temp_list.append(stack.pop())
    temp_list.reverse()
    for i in range(len(temp_list)):
        if temp_list[i] == "-":
            temp_list[i] = "+"
        else:
            temp_list[i] = "-"
    for null in range(len(temp_list)):
        stack.append(temp_list.pop())
    print(stack)


def flip(stack):
    top_count = 0
    for i in range(len(stack)):
        if stack[i] == "-":
            break
        top_count += 1
    top_count = len(stack) - top_count
    temp_list = []
    for null in range(top_count):
        temp_list.append(stack.pop())

    temp_list.reverse()

    for i in range(len(temp_list)):
        if temp_list[i] == "-":
            temp_list[i] = "+"
        else:
            temp_list[i] = "-"
    for null in range(len(temp_list)):
        stack.append(temp_list.pop())

def test_plus(stack):
    k = -1
    for i in range(-1, -(len(stack)), -1):
        if stack[i] == "-":
            k = i + 1
            break
    if "-" not in stack[k:]:
        return True

if __name__ == '__main__':
    # read input
    with open('input.txt', 'rt') as fin:
        numCases = int(fin.readline())
        stackList = []
        for i in range(numCases):
            cur_stack = list(fin.readline().strip())
            cur_stack.reverse()
            stackList.append(cur_stack)
    print(stackList)

    outputString = ""
    for stack, i in zip(stackList, range(len(stackList))):
        count = 0
        while True:
            if "-" not in stack:
                break
            else:
                if test_plus(stack):
                    flip_plus(stack)
                    count += 1
                    continue
                flip(stack)
                count += 1

        outputString += "Case #" + str(i + 1) + ": " + str(count) + "\n"

    fout = open('output.txt', 'wt', encoding='utf-8')
    fout.write(outputString)
    fout.close()
