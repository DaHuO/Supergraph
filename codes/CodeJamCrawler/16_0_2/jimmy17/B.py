tests = int(raw_input())

for i in range(tests):
    result = 0
    pancakes = raw_input()
    state = pancakes[0]
    has_changed = False
    plus_exists = False
    for ch in pancakes:
        if ch != state:
            has_changed = True
            if state == '+':
                plus_exists = True
                result += 2
            else:
                if not plus_exists:
                    result += 1
            state = ch
    if has_changed == False and state == '-':
        result = 1

    print 'Case #'+ str(i+1)+': '+ str(result)
