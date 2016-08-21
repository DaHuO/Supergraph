f = open("A-large.in", "r")
num_lines = int(f.readline())

def calc(num):
    digits = [False] * 10

    i = 1
    while sum(digits) != 10:
        for d in [int(d) for d in list(str(i*num))]:
            digits[d] = True
        i+=1
    return (i-1)*num

for i in range(num_lines):
    num = int(f.readline())
    if num == 0:
        ans_str = "INSOMNIA"
    else:
        ans_str = str(calc(num))
    
    print "Case #" + str(i+1) + ":", ans_str
