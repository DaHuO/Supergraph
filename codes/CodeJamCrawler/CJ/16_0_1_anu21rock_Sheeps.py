def solve(N):
    i = 0 
    whole_set =set([])
    while True:
        if len(whole_set) == 10: 
            return i * N
            break
        x = (i+1) * N
        whole_set = whole_set | set(str(x))
        i += 1
        if i > 10 **6 : 
            return "INSOMNIA"
            break

test = int(raw_input())
for test_num in range(test):
    value = int(raw_input())
    print "Case #%d: "%((test_num+1)), solve(value)

