for _ in range(int(input())):
    inp = raw_input().replace('-','0').replace('+','1')+'1'
    turns = 0
    for i in range(len(inp)-1):
        if inp[i+1]!=inp[i]:
            turns += 1
    print('Case #{}: {}'.format(_+1,turns))