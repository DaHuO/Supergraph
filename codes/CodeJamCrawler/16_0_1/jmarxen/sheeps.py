
def solve_case(i):
    if i == 0:
        return "INSOMNIA"
    
    v = i
    seen = [False]*10
    while not all(seen):
        s = str(v)
        for x in s:
            seen[ord(x) - ord('0')] = True
        v += i
        
    return s

num_cases = input()
cur_case = 1
while cur_case <= num_cases:
    print "Case #"+str(cur_case)+": "+solve_case(input())
    cur_case += 1