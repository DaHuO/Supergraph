
def reduce_stack(s):
    previous = None
    stack = []
    count = 0
    for k in range(len(s)):
        if s[k] == previous:
            count += 1
        else:
            # push current count on stack
            if previous:
                stack += [(previous, count)]
            count = 1
            previous = s[k]
    stack += [(previous, count)]
    return stack

def pancakes(s):
    stack = reduce_stack(s)
    if stack[-1][0] == '+':
        stack = stack[:-1]
    return str(len(stack))
    
def main():
    t = int(raw_input())
    for k in range(t):
        s = raw_input().strip()
        print 'Case #' + str(k+1) + ': ' + pancakes(s)

if __name__ == '__main__':
    main()

