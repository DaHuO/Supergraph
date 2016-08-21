
flip_count = 0

def main():
    global flip_count
    f = open('Input.txt', 'r')
    f2 = open('Output.txt', 'w')
    num_lines = int(f.readline())
    for i in range(num_lines):
        case = f.readline().strip()
        flip_count = 0
        case = group(case)
        while len(case) > 3 or ('-' in case):
            if len(case) > 3:
                case = flip(case[:3]) + case[3:]
            else:
                case = flip(case[0]) + case[1:]
            case = group(case)
        f2.write('Case #' + str(i + 1) + ': ' + str(flip_count) + '\n')


    f.close()
    f2.close()
    print('done')


def group(case):
    grouped_case = []
    grouped_case.append(case[0])
    for el in range(1, len(case)):
        if case[el] != grouped_case[-1]:
            grouped_case.append(case[el])
    return(grouped_case)
    

def flip(part):
    global flip_count
    flip_count += 1
    fliped_part = []
    for ch in part:
        if ch == '-':
            fliped_part.append('+')
        else:
            fliped_part.append('-')
    return(fliped_part)


main()
