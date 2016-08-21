__author__ = 'Austin'

# main method
f_in = open('p1.txt')
noOfTestCases = int(f_in.readline())
f_out = open('p1_out.txt', 'w')
for t in range(0, noOfTestCases):
    input_str = f_in.readline()
    output = 0
    n = int(input_str)
    digits = set()
    for j in range(1, 100):
        k = n*j
        while k > 0:
            digits.add(int(k % 10))
            k = int(k/10)
        if len(digits) == 10:
            output = n*j
            break
    if output == 0:
        output = 'INSOMNIA'
    # write to file
    f_out.write('Case #'+str(t+1)+": "+str(output)+"\n")

# close files
f_in.close()
f_out.close()

