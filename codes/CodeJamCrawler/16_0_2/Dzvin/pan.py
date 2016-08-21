from linkedstack import LinkedStack
with open('B-large.in', 'r') as f:
    t = int(f.readline())

    lst_cases = []
    for line in f:
        lst = []
        stk = LinkedStack()
        line = line.strip()
        case = line

        for j in range(len(case)):
            if case[j] == '+':
                lst.append(1)
            else:
                lst.append(-1)
        lst.reverse()
        for item in lst:
            stk.push(item)
        lst_cases.append(stk)
def main(case):
    num_man = 0
    if case.sum()  == - len(case):
        return 1
    while True:
        if case.sum() == len(case):
            return num_man

        item = case.pop()
        lst_popped = [ -item]
        next_item = case.peek()
        while item == next_item:
            case.pop()
            lst_popped.append(-next_item)
            item = next_item
            if case.isEmpty():
                break
            next_item = case.peek()
        for item in lst_popped:
            case.push(item)
        num_man += 1

i = 1
for case in lst_cases:
    print('Case #' + str(i) + ': ' + str(main(case)))
    i += 1
