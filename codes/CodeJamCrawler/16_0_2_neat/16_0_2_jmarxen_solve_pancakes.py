
def solve_case(s):
    boundars = 0
    i = 0
    while i < len(s) - 1:
        if s[i] != s[i+1]:
            boundars += 1
        i += 1
    
    if s[-1] == "-":
        boundars += 1
        
    return str(boundars)

num_cases = input()
cur_case = 1
while cur_case <= num_cases:
    print "Case #"+str(cur_case)+": "+solve_case(raw_input().strip())
    cur_case += 1