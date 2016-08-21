# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def md(counter,letter,digit):
    counter[letter] -= phone_digits[digit]
    return

def md2(counter,rest,digit):
    for s in rest:
        md(counter,s,digit)

for i in xrange(1, t + 1):
    phone_number = raw_input()
    phone_digits = [0 for _ in range(10)]
    dict_count = {}
    for s in alphabet:
        dict_count[s] = 0
    for s in phone_number:
        dict_count[s] += 1
    phone_digits[0] = dict_count['Z']
    md2(dict_count,'ERO',0)

    phone_digits[2] = dict_count['W']
    md(dict_count,'T',2)
    md(dict_count,'O',2)

    phone_digits[6] = dict_count['X']
    md2(dict_count,'SI',6)

    phone_digits[8] = dict_count['G']
    md2(dict_count,'EIHT',8)

    phone_digits[3] = dict_count['H']
    md2(dict_count,'TREE',3)

    phone_digits[4] = dict_count['U']
    md2(dict_count,'FOR',4)

    phone_digits[5] = dict_count['F']
    md2(dict_count,'IVE',5)

    phone_digits[7] = dict_count['V']
    md2(dict_count,'SEEN',7)

    phone_digits[1] = dict_count['O']
    md2(dict_count,'NE',1)

    phone_digits[9] = dict_count['E']
    md2(dict_count,'NIN',9)
    substrings = [str(x[0])*x[1] for x in zip(range(10),phone_digits)]
    print "Case #{}: {}".format(i, "".join(substrings))
