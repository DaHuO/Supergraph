T = int(input())
for tc in range(1,T+1):
    chars = []
    chars.extend(input())

    count = 0
    above = chars[0]
    
    if above == '-':
        arrChar = [0]
    else:
        arrChar = [1]
    
    for i in chars:
        if i == '-':
            if above == '+':
                count += 1
                arrChar.append(0)
                above = '-'
        else:
            if above == '-':
                count += 1
                arrChar.append(1)
                above = '+'

    above = arrChar[0]
    jawab = 0
    for i in arrChar:
        if not i:
            if i == above:
                jawab += 1
            else:
                jawab += 2
        above = "+"       
        
    print("Case #{0}: {1}".format(tc, jawab))