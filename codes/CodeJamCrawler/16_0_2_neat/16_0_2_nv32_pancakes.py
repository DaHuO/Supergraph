def print_case(i,result):
    print("Case #" + str(i) + ": " + str(result))

def read_test_cases():
    test_cases = []
    T = raw_input();
    for i in range(0,int(T)):
        test_cases.append(raw_input())
    return test_cases

def toggle(c):
    if c == '+':
        return '-'
    elif c == '-':
        return '+'
    else:
        return None

def flip_top_n(stack,n):
    return ''.join([toggle(x) for x in stack[n-1::-1]]) + stack[n:]

def solve_test_case(n,test_case):
    flips = 0
    temp = test_case
    while True:
        # trim trailing "+"s
        temp = temp.rstrip('+')
        if temp == "":
            print_case(n,flips)
            return
        if temp[0] == '-':
            # if starting with "-"s, flip all
            temp = flip_top_n(temp,len(temp))
        else:
            # if starting with "+"s, flip all of them
            temp = flip_top_n(temp,len(temp)-len(temp.lstrip('+')))
        flips += 1

def main():
    test_cases = read_test_cases()
    test_case_counter = 1
    for t in test_cases:
        solve_test_case(test_case_counter,t)
        test_case_counter += 1

main()
