import math

fl_o = open("output.txt", 'w')

def conv_base(num_arr, i):
    x = 0
    for j in num_arr:
        x = x*i + j
    return x

def find_fact(dec):
    for i in xrange(2, int(1+math.sqrt(dec))):
        if dec%i == 0: return i
    return 1

def print_all(num_arr):
    fl_o.write(str(conv_base(num_arr, 10)))
    for i in range(2, 11):
        dec = conv_base(num_arr, i)
        f = find_fact(dec)
        fl_o.write(" "+str(f))
    fl_o.write("\n")

def check_if_all_set(num_arr):
    for i in range(2, 11):
        dec = conv_base(num_arr, i)
        f = find_fact(dec)
        if f == 1: return False
    return True

def num_to_arr(num):
    arr = []
    while num > 0:
        rem = num%2
        num = num/2
        arr.insert(0, rem)
    return arr

def calc(file):
    n, j = map(int, file.readline().split())
    num = 1 + pow(2, 15)
    while True:
        if j == 0: break
        num_arr = num_to_arr(num)
        if check_if_all_set(num_arr):
            print_all(num_arr)
            j -= 1
        num += 2

def main():
    file = open("input.txt")
    T = int(file.readline())
    for t in range(T):
        fl_o.write("Case #" + str(t+1) + ":" + "\n")
        calc(file)
    fl_o.close()

main()
