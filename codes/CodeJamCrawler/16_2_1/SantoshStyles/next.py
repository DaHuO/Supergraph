
with open('C:\Users\santosh\PycharmProjects\GoogleCodeJam\A-large.in') as f:
    content = f.readlines()

f1=open('C:\Users\santosh\PycharmProjects\GoogleCodeJam\outnext2.txt', 'w+')

def stuff(here):
    testcase= here
    number = []
    while ( 'Z' in testcase and 'E' in testcase and 'R' in testcase and 'O' in testcase):
        upto = len(testcase)
        for i in range(0,upto):
            if testcase[i] == 'Z':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'E':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'R':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'O':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        number.append(0)

    while ( 'T' in testcase and 'W' in testcase and 'O' in testcase):
        upto = len(testcase)
        for i in range(0,upto):
            if testcase[i] == 'T':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'W':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'O':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        number.append(2)

    while ( 'E' in testcase and 'I' in testcase and 'G' in testcase and 'H' in testcase and 'T' in testcase):
        upto = len(testcase)
        for i in range(0,upto):
            if testcase[i] == 'E':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'I':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'G':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'H':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'T':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        number.append(8)

    while ( 'S' in testcase and 'I' in testcase and 'X' in testcase):
        upto = len(testcase)
        for i in range(0,upto):
            if testcase[i] == 'S':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'I':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'X':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        number.append(6)

    while ( 'T' in testcase and 'H' in testcase and 'R' in testcase and 'E' in testcase and 'E' in testcase):
        upto = len(testcase)
        for i in range(0,upto):
            if testcase[i] == 'T':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'H':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'R':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'E':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'E':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        number.append(3)

    while ( 'F' in testcase and 'O' in testcase and 'U' in testcase and 'R' in testcase):
        upto = len(testcase)
        for i in range(0,upto):
            if testcase[i] == 'F':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'O':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'U':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'R':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        number.append(4)

    while ( 'F' in testcase and 'I' in testcase and 'V' in testcase and 'E' in testcase):
        upto = len(testcase)
        for i in range(0,upto):
            if testcase[i] == 'F':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'I':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'V':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'E':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        number.append(5)

    while ( 'S' in testcase and 'E' in testcase and 'V' in testcase and 'E' in testcase and 'N' in testcase):
        upto = len(testcase)
        for i in range(0,upto):
            if testcase[i] == 'S':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'E':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'V':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'E':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'N':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        number.append(7)

    while ( 'O' in testcase and 'N' in testcase and 'E' in testcase):
        upto = len(testcase)
        for i in range(0,upto):
            if testcase[i] == 'O':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'N':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'E':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        number.append(1)

    while ( 'N' in testcase and 'I' in testcase and 'N' in testcase and 'E' in testcase ):
        upto = len(testcase)
        for i in range(0,upto):
            if testcase[i] == 'N':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'I':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'N':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        for i in range(0,upto):
            if testcase[i] == 'E':
                b = bytearray(testcase)
                del b[i]
                testcase=str(b)
                break
        number.append(9)
    return number




for j in range (1, len(content)):
    answer = stuff(content[j])
    sortednumber =sorted(answer, key=int)
    str1 = ''.join(str(e) for e in sortednumber)
    f1.write('Case #'+str(j)+': '+str(str1)+'\n')