def count_steps(state):
    steps = 0
    current_symbol = '+'
    
    for c in reversed(state):
        if c != current_symbol:
            current_symbol = c
            steps += 1
    
    return steps


def main():
    count = int(input())
    
    for i in range(count):
        current = input()
        print('Case #%d: %s' % (i + 1, count_steps(current)))

if __name__ == '__main__':
    main()