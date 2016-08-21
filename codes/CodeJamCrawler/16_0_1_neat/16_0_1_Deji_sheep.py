def count_sheep(N):
    check_val = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if N == 0:
        return "INSOMNIA"
    
    i = 1
    while True:
        val = str(i*N)
        i += 1
        rm_list = [num for num in check_val if val.find(num) != -1] 
        check_val = list(set(check_val)-set(rm_list))
            
        if check_val == []:
            return val

n_cases = int(raw_input())

for i in range(1, n_cases+1):
    N = int(raw_input())
    print "Case #%d: %s" %(i, count_sheep(N))
