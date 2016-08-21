def invert(pancakes):
    new_pan=[]
    for pan in pancakes:
        if pan=='-':
            new_pan.append('+')
        else:
            new_pan.append('-')

    if len(new_pan)==2:
        return ''.join(new_pan)
    else:
        return ''.join(new_pan)[::-1]

for case in range(1, int(raw_input())+1):
    cur_stack=raw_input().strip();
    N=len(cur_stack);
    count=0;
    while '-' in cur_stack:
        if cur_stack[0]=='+':
            cur_pan_ind=cur_stack.find('-')-1
        else:
            cur_pan_ind=cur_stack.rfind('-') 

        if cur_pan_ind+1==N:
            if cur_stack[0]=='+':
                print('special')
                cur_stack_start=invert(cur_stack[0])
                cur_stack_end=cur_stack[1:]
                cur_stack=cur_stack_start+cur_stack_end
                count+=1
            cur_stack=invert(cur_stack)
            count+=1
        else:
            cur_stack_start=invert(cur_stack[0:cur_pan_ind+1])
            cur_stack_end=cur_stack[cur_pan_ind+1:]
            cur_stack=cur_stack_start+cur_stack_end
            count+=1

    print 'Case #{}: {}'.format(case,count)         