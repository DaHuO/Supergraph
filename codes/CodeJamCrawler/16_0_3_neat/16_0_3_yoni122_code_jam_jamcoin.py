import math
import itertools
import time




def divider(n):
    #print "looking for divider for: {0}".format(n)
    if n % 2 == 0 and n > 2:
        return 2
    max = int(math.sqrt(n)) + 1
    j = 1
    for i in itertools.count(3, 2):
        if i >= max:
            break
        if j % 1000000 == 0:
            print "Checking if {0} divides by {1}".format(n, i)
            print "returning"
            return -1
        j += 1
        if n % i == 0:
            return i
    return -1

def generate_jamcoin(N, J):

    x = 0
    jamcoin_dict = {}
    jamcoin_num = 0
    max = 2 ** (N - 2)
    for i in itertools.count(0):
        divider_list = []
        if (i >= max):
            break
        x = "1{0:0{1}b}1".format(i, N - 2)
        res = True
        if i % 10 == 0:
            print "checking num {0} time: {1}".format(i, round(time.time()))
        for j in xrange(2, 11):
            num = int(x, j)
            d = divider(num)
            if d == -1:
                res = False
                break
            divider_list.append(d)

        if i % 10 == 0:
            print "checking  num {0} time: {1}".format(i, round(time.time()))

        if res == True:
            jamcoin_dict[x] = divider_list
            jamcoin_num += 1
            print "Found {0} so far at number {1}".format(jamcoin_num, i)
            if jamcoin_num == J:
                return jamcoin_dict

    return {}


def main(input_file, output_file):

    with open(input_file) as input:
        number_list = input.readlines()

    print "Got {0} input numbers".format(number_list[0])


    number_list.pop(0)

    jamcoin_dict = generate_jamcoin(32, 500)

    print "Case #{0}:"
    for key in jamcoin_dict:
        print key , ' '.join(str(ch) for ch in jamcoin_dict[key])


    with open (output_file, 'w') as output:
        output.write( "Case #1:\n")
        for key in jamcoin_dict:
            output.write("{0} {1}\n".format(key, ' '.join(str(ch) for ch in jamcoin_dict[key])))
    return


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    main(input_file, output_file)
