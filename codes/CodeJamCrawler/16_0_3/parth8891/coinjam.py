import itertools
import math

class FileHandling:

    def __init__(self, filename='3_input.txt', ofilename='3_output.txt'):
        self.filename = filename
        self.ofilename = ofilename
        self.fw = open(filename, "r")
        self.ofw = open(ofilename, "w")
        self.ofw.close()

    def log_msg(self, msg):
        with open(self.ofilename, "a") as self.ofw:
            self.ofw.write(msg + "\n")

    def read(self):
        return self.fw.readline()

    def __del__(self):
        self.fw.close()

def get_div(num):
    if num % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return i
    return -1

def check_prime(num_st):
    l = []
    for i in range(2,11,1):
        num = int(num_st, i)
        #print(int(num_st, i))
        ans = get_div(num)
        if ans == -1:
            return (False,l)
        else:
            l.append(ans)
    return(True,l)


f = FileHandling()
_size = int(f.read())
for i in range(_size):
    line = f.read()
    sl = line.split(" ")
    n = int(sl[0])
    lst = list(itertools.product([0, 1], repeat=(n-2)))
    #print(lst)
    index = 0
    j = 1
    f.log_msg("Case #{}:".format(i+1))
    while j <= int(sl[1]):
        t = (1,)+lst[index]+(1,)
        print(t)
        str_tp = ''.join(map(str, t))
        print(str_tp)
        tpans=check_prime(str_tp)
        if tpans[0]:
            print(str_tp,' '.join(map(str, tpans[1])))
            j += 1
            f.log_msg(str_tp+" "+' '.join(map(str, tpans[1])))
        index +=1