def perform(s):
    global count
    if s[0]=='+':
        ind = s.index('-')
        s[:ind] = ['-']*ind
    else:
        ind = len(s)-s[::-1].index('-')
        j = 0
        for i in s[:ind][::-1]:
            if i =='+':
                    s[j]='-'
                    j+=1
            else:
                    s[j]='+'
                    j+=1
    return s
for _ in range(input()):
    count = 0
    s = raw_input()
    s = list(s)
    while('-' in s):
        count+=1
        s = perform(s)
    print 'Case #%d:'%(_+1),count
        
    
