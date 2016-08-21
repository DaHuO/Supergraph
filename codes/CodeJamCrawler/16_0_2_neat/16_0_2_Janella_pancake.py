

def main() -> None:
    outfile = open('pancake_output.out', 'w')
    name = input()
    case = open(name, 'r')
    caselist = case.readlines()
    tests = int(caselist[0])
    count = 0
    for c in caselist[1:]:
        count += 1
        outfile.write('Case #{}: {}\n'.format(count, pancake(c.strip())))
    case.close()
    outfile.close()

def pancake(stack: str ) -> str:
    up = '+'
    down = '-'
    counter = 0
    
    while( not all(p == up for p in stack)):
        if stack[-1] == down and stack.count(down) >= stack.count(up):
            stack = flip(stack)
            counter += 1
        elif stack[-1] == up:
            stack = stack[:-1]
        else:
            stack = flip(stack)
            counter += 1
    return counter
    

def flip(stack: str) -> str:
    return stack.translate(str.maketrans('+-', '-+'))


main()

