for t in range(int(input())):       # First input is the number of cases.
    config = input()                # config is the starting config of pancakers.
    count  = 0
    length = len(config)
    front = 0
    index = 0
    while front < length:
        if config[index] == '+':
            front = front + 1
            index = index + 1
        else:
            temp = index
            while config[temp] == '-':
                temp = temp + 1
                if temp > length-1:
                    break
            if front == 0:
                count = count + 1
            else:
                count = count + 2
            front = min(length, temp)    
            index = front
    print("Case #%d: %d"%(t+1, count))
        
