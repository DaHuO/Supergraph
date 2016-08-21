def rotate(l):
    h = l[::-1]
    for ch in range(len(h)):
        if h[ch] == '+':
            h[ch] = '-'
        else:
            h[ch] = '+'
    return h

cases = int(input())

for x in range(int(cases)):
    
    steps = 0
    heap = list(input())
    length = len(heap)
    
    if '-' not in heap:
        print("Case #" + str(x+1) + ": " + str(0))
        continue

    if '+' not in heap:
        print("Case #" + str(x+1) + ": " + str(1))
        continue
    
    while '+' in heap:
        
        symbol_to_find = '+'
        
        if heap[0] == symbol_to_find:
            if symbol_to_find == '+':
                symbol_to_find = '-'
            else:
                symbol_to_find = '+'

        i = heap.index(symbol_to_find)   
        symbol_next = i
        
        for ch in range(i, length - 1):
            if heap[i] == symbol_to_find:
                symbol_next += 1

        
              
        to_rotate_part = heap[:i]
        heap = rotate(to_rotate_part) + heap[i:length]
        steps += 1
                
        if '+' not in heap:
            steps += 1
            break
        if '-' not in heap:
            break     
            
    print("Case #" + str(x+1) + ": " + str(steps))
