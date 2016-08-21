def last_num(N):
    cur_num = 0
    seen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    done = False
    
    while not done:
        cur_num = cur_num + N
        cur_num_str = str(cur_num)
        for i in range(len(cur_num_str)):
            seen[int(cur_num_str[i])] = 1
        done = True
        for b in seen:
            if b is 0:
                done = False

    return cur_num


T = int(input(""))

for i in range(T):
    N = int(input(""))
    if N is 0:
        print("Case #" + str(i+1) + ": INSOMNIA")
        continue
    print("Case #" + str(i+1) + ": " + str(last_num(N)))
    
