import sys

name="./small.txt"

def checkPrime(num):
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in xrange(2, 200):
            if (num % i) == 0:
                return num/i
  
    return -1

def computeallbases(value):

    mdict = {}

    for ii in xrange(2, 11):
        #res = 0
        #for i in xrange(len(value) - 1):
        #    res = res + pow(value[len(value) - 1 - i], ii)
        #ret = checkPrime(res)
        ret = checkPrime(int(value, ii))
        if ret < 0:
            # number is prime, should check a new one
            return -1, {}
        mdict[ii] = ret
    return 0, mdict


class persResult(object):
    def __init__(self, mstring, bases):
        self.mstring = mstring
        self.bases = bases

    def __str__(self):
        res = self.mstring + " "
        for ii in xrange(2, 11):
            res = res + str(self.bases[ii]) + " "
        return res


def algo1(tt, coins, lght):

    buff = []

    # should build n strings with lenght lght.
    # String should begon-end with 1, then should be checked for all bases
    # and should have have a divisor for each base

    mstring = "1"
    for _ in xrange(lght-2):
        mstring = mstring + "0"
    mstring = mstring + "1"

    relative_int_value = int(mstring, 2)

    found = 0
   
    checking = 0

    while(True):
        #test string
        res, mdict = computeallbases(mstring)
        if res == 0:
            buff.append(persResult(mstring, mdict))
            found = found + 1
            print("Found {0} res".format(found))
            if found == coins:
                return 0, buff
        # change string, test again
        relative_int_value = relative_int_value + 2
        mstring = bin(relative_int_value)[2:]
        checking = checking + 1
        if checking % 1 == 0:
            print("checking {0}\nbin {1}".format(relative_int_value, mstring))



def check():
    fl_wrt = open(name + "_reply", 'r')
    fl_real = open(name + "_real", 'r')

    for line_1 in fl_wrt.readline():
        line_2 = fl_real.readline()
        if line_2 != line_1:
            print('Line do not match:\n{0}{1}'.format(line_1, line_2))

    fl_real.close()
    fl_wrt.close()

def main():

    global name

    if len(sys.argv) > 1:
        #if sys.argv[1] == 'check':
        #    check()
        #    return 0
        #else:
        name = sys.argv[1]

    fl = open(name, 'r')
    fl_wrt = open(name + "_reply", 'w')

    tt = int(fl.readline())
    i = 0

    reply = ''

    while (i < tt):
        i = i+1
      
        numb = fl.readline().rstrip().split()
        numb = [int(a) for a in numb]
        lght = numb[0]
        coins = numb[1]

        res1, buff = algo1(tt, coins, lght)
        mbuffer = ""
        for res in buff:
            mbuffer = mbuffer + str(res) + "\n"

        reply = reply + "Case #{0}:\n{1}".format(i, mbuffer)

    fl_wrt.write(reply)

    fl.close()
    fl_wrt.close()


if __name__ == "__main__":
    main()
