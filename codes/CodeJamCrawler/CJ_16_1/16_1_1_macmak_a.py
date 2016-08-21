T = int(input())

for case in range(T):
    string = input()
    out = ''
    for c in string:
        if out == '':
            out = c
            continue
        if c >= out[0]:
            out = c + out
        else:
            out = out + c
    print('Case #',case+1,': ',out,sep='')
