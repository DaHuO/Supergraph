cases = int(raw_input().strip())
out = open('output.txt', 'w')

for case in range(cases):
    orig = int(raw_input().strip())
    digits = list(range(0, 10))

    num = orig
    res = False

    for i in range(1000000):
        for c in str(num):
            try:
                digits.remove(int(c))
            except:
                pass
        if digits == []:
            res = num
            break
        num += orig

    if res:
        s = "Case #"+str(case+1)+": "+str(num)+"\n"
    else:
        s = "Case #"+str(case+1)+": "+"INSOMNIA"+"\n"
    out.write(s)
    print(s)
