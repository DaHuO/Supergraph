for _ in range(int(input())):
    text = list(raw_input())
    pt = text[0]
    print('Case #{}:'.format(_+1)),
    for i in text[1:]:
        #print i,pt[0]
        if i < pt[0]:
            pt = pt+i;
        else:
            pt =  i+pt
    print pt