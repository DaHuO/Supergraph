size = int (raw_input())




def processlastword(s):
    ls = [c for c in s]
    sn = ''
    for c in ls:
        if sn == '':
            sn = c
            continue
        if c >= sn[0]:
            sn = c+sn
        else:
            sn = sn + c
    return sn





i=0
while True:
    if i>=size:
        break
    i = i+1
    print 'Case #'+ str(i) + ': ' + processlastword(raw_input())
