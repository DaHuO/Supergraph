def cut(myStr):
    i = 0
    for i in range(len(myStr) - 2, -1, -1):
        if myStr[i] != '+':
            break

    if i == 0 and myStr[0] == '+':
        return ''
    else:
        return myStr[0 : i + 1]

def fingConsPos(myStr):
    consPos = -1
    consRec = 0
    consBig = 0
    on = False;
    for i in range(0, len(myStr)):
        if myStr[i] == '+' and on == False:
            on = True
            consBig += 1
        elif myStr[i] == '+' and on == True:
            consBig += 1
        elif myStr[i] == '-' and on == True:
            if consBig > consRec:
                consRec = consBig
                consPos = i - 1;
            consBig = 0
            on = False
    return consPos

def reverse(myStr, start, end):
    ans = ''
    for i in range(0, start):
        ans += myStr[i]
    for i in range(end, start - 1, -1):
        if myStr[i] == '+':
            ans += '-'
        elif myStr[i] == '-':
            ans += '+'
    for i in range(end + 1, len(myStr)):
        ans += myStr[i]
    return ans

def main():
    myInput = open('B-large.in', 'r')
    myOutput = open('outputLarge.txt', 'w')
    T = myInput.readline();
    case = 0
    for S in myInput:
        case += 1
        ans = 0
        S = cut(S)
        while len(S) > 0:
            consPos = fingConsPos(S)
            if consPos == -1:
                ans += 1
                break
            elif S[0] == '-':
                S = reverse(S, 0, len(S) - 1)
                ans += 1
                S = cut(S)
            else:
                S = reverse(S, 0, consPos)
                ans += 1
                S = reverse(S, 0, len(S) - 1)
                ans += 1
                S = cut(S)
        # print("Case #%d: %d" % (case, ans))
        myOutput.write("Case #%d: %d\n" % (case, ans))

    myInput.close()
    myOutput.close()



main()
