def counting_sheep(number):
    if number == 0:
        return "INSOMNIA"
    digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    digit_check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(10000000):
        digit_split = list(str(number*(i+1)))
        for j in range(len(digit_split)):
            num = digit_split[j]
            digit_check[digit.index(int(num))] = 1
            array_sum = sum(digit_check)
            #print i,number*(i+1), digit_check
            if array_sum == 10:
                return str(number*(i+1))
                break
    return "INSOMNIA"

fp = open("A-large.in", "r")

fout = open("output_large.txt", "w")
num_lines = int(fp.readline())
for i in range(num_lines):
    num = int(fp.readline())
    str_out = "Case #%d: %s\n" % ((i+1),counting_sheep(num))
    print str_out
    fout.write(str_out)

fp.close()
fout.close()