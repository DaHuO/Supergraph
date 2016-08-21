output = []

test = int(input().strip())

for i in range(test):
    s = input().strip()
    count = 0
    state = "+"
    symbol = "+"

    for j in range(len(s)-1, -1, -1):
        if s[j] == symbol:
            continue
            
        elif s[j] != state:
            count += 1
            if state == '+':
                state = '-'
            else:
                state = '+'

            symbol = s[j]

    str1 = "Case #" + str(i+1) + ": " + str(count)
    output.append(str1)



for i in output:
    print (i)
