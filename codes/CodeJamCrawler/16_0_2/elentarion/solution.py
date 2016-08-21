nb_test_cases = int(raw_input())

def recurse_flip(op, stack):
    if '-' in stack:
        stack = stack[:''.join(stack).rindex('-') + 1]
    else:
        return op
        
    count_minus = ''.join(stack).count('-')
    count_plus = ''.join(stack).count('+')
    
    if count_plus < count_minus:
        return recurse_flip(op + 1, flip(stack, len(stack)))
    else:
        last_plus = ''.join(stack).rindex('+')
        return recurse_flip(op + 1, flip(stack, last_plus + 1))

def flip(stack, to):
    return [ ('+' if pancake == '-' else '-') for pancake in reversed(stack[:to]) ] + stack[to:]

for case_number in range(1, nb_test_cases + 1):
    stack = list(raw_input())

    # jop = recurse_flip(0, stack)
    op = 0
    i = len(stack) - 1
    ref_stack = ['+'] * len(stack)
    while i >= 0:
        if ref_stack[i] != stack[i]:
            ref_stack = flip(ref_stack, i)
            op += 1

        i -= 1 
    
    print 'Case #%d: %d' % (case_number, op)