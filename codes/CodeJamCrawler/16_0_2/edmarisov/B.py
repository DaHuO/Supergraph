def process(input):
    input = input.replace('\n', '')
    while True:
        final = input
        input = input.replace('--', '-')
        input = input.replace('++', '+')
        if final == input:
            break;
    
    count = 0
    was_plus = False
    for c in input:
        if c == '-':
            count = count + 1
            if was_plus:
                count = count + 1
        elif c == '+':
            was_plus = True
    
    return count
    
    
if __name__ == '__main__':
    res = ''
    i = 0
    with open('B-large.in', 'r') as file:
        first = True
        for line in file:
            if first:
                first = False
                continue;
            i = i + 1
            res = res + ("Case #%s: %s\n" % (i, process(line)))

    with open('output', 'w+') as file:
        print res
        file.write(res)