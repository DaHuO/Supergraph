file = open("A-large.in")
lines = file.read().split("\n")
out = open("output", 'w')
for case in range(1,int(lines[0])+1):
    if lines[case]=="0":
        print("Case #" + str(case) + ": INSOMNIA")
        out.write("Case #" + str(case) + ": INSOMNIA" + '\n')
        continue
    org = int(lines[case])
    num = 0
    digits = [0,0,0,0,0,0,0,0,0,0]
    while 0 in digits:
        num = num+org;
        for digit in str(num):
            digits[int(digit)]=1
    print("Case #" + str(case) + ": " + str(num))
    out.write("Case #" + str(case) + ": " + str(num) +'\n')
out.close()
