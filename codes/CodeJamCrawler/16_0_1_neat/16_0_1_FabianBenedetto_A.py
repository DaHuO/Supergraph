import pdb;

all_digits = {0,1,2,3,4,5,6,7,8,9}

def get_digits(N,case_number):
    digits = set()
    N_i = N
    while True:
        if N == 0:
            return "Case #" + str(case_number) + ": INSOMNIA"
        for dig in str(N_i):
            digits.add(int(dig))
        if digits == all_digits:
            return "Case #" + str(case_number) + ": " + str(N_i)
        N_i += N

i = 0
f_read = open("numbers2.txt")
f_write = open("Result_A_large.txt","w")
for line in f_read:
    if i == 0:
        i = 1
        continue
    #pdb.set_trace()
    buff = get_digits(int(line),i)
    f_write.write(buff)
    f_write.write("\n")
    i += 1
