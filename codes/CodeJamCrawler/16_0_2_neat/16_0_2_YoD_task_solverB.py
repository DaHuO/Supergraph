t = int(input())  
test_stacks = []

def print_result(test,result):
    print("Case #{}: {}".format(test, result))
    
    
def happy_pancakes(pancakes_stack):
    if pancakes_stack.find('0') == -1:
        return False
    else:
        return True
        
def flip_startn_pancakes_in_stack(n,stack):
    
    new_stack_part1 = stack[0:n]
    new_stack_part2 = stack[n:][::-1] 
    new_stack_part3 = ''
    for el in new_stack_part2:
        if el == '0':
            new_stack_part3 += '1'
        else:
            new_stack_part3 += '0'
    # print("P1 {} P2 {}".format(new_stack_part1,new_stack_part3))
    return new_stack_part1 + new_stack_part3
            
            
def solve_problem(element):
    flip = 0
    search_el = '0'
    s_start = 0
    l = len(element)
    while happy_pancakes(element):
        
        not_happy_pancake = element.find(search_el,s_start)
        if not (not_happy_pancake == -1):
            if element[l-1] == element[not_happy_pancake]:
                # print("New {} hp {} flip {}".format(element,not_happy_pancake,flip))
                element = flip_startn_pancakes_in_stack(not_happy_pancake,element)
                flip += 1
                s_start = 0
                search_el = '0'
            else:
                s_start = not_happy_pancake
                search_el = '1'
            
        else:
            break
            
    
    return flip
        
        
        
    
for i in range(0, t):
    temp = input()
    temp = temp.replace('-',"0")
    temp = temp.replace('+',"1")[::-1]
    test_stacks.append(temp)
    
# print(test_stacks)
for i in range(0,t):
    res = solve_problem(test_stacks[i])
    print_result(i+1,res)
    