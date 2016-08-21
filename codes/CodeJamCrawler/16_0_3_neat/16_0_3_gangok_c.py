import math

prime_dict = dict()

infile = open("input.txt", "r")
outfile = open("output.txt", "w")
data = infile.readlines()
T = int(data[0])

def increase(string):
    n = len(string)
    
def check_prime(number):
    if number in prime_dict:
        return prime_dict[number]
    #for_max = int(math.sqrt(number))
    for_max = 10000
    i = 2
    while i < for_max + 1:
        if number % i == 0:
            prime_dict[number] = i
            return i
        i += 1
    prime_dict[number] = -1
    return -1

def run(N, J):
    now_string = "1" + "0"*(N-2) + "1"
    now_num = int(now_string, 2)
    now_solution = []
    ret = []
    while True:
        now_solution = []
        for base in range(2, 11):
            num_in_base = int(now_string, base)
            div = check_prime(num_in_base)
            if div == -1:
                break
            else:
                now_solution.append(div)

        if len(now_solution) == 9:
            ret.append([now_string, now_solution])
            print len(ret)
            if len(ret) >= J:
                return ret
        now_num += 2
        now_string = bin(now_num)[2:]
        if len(now_string) > N:
            break

for t in range(T):
    N = int(data[t+1].split()[0])
    J = int(data[t+1].split()[1])
    ret = run(N, J)
    outfile.write("Case #" + str(t+1) + ":\n")
    for i in range(J):
        outfile.write(ret[i][0] + " ")
        for j in range(9):
            outfile.write(str(ret[i][1][j]) + " ")
        outfile.write('\n')
    print ret

infile.close()
outfile.close()
