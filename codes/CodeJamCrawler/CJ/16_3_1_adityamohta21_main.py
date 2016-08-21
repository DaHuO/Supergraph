# ------Notes------
# use any_string.zfill(int)  to print the string in given number of digits as arguement.
# " ".join(list) to convert list to string
# for k,v in dic.items() k is key and v is value of dictionary dic
# filter(lambda x: x % 3 == 0, foo) where foo is a list of numbers.
# print map(lambda x: x * 2 + 10, foo) returns changed values of list foo.
# reduce(lambda x, y: x + y, foo) returns the addition of list foo.
# Bitwise operators:    ~ Not, ^ XOR, | Or, & And
# int('1000110',2) to get the value of the number in base 2 (i this case 70)we can say binary to decimal convertion.
# bin(a & b) to do binary calculations.
# to add a value in a sorted list in a sorted manner. # from bisect import bisect
# bisect(b, a, lo=0, hi=len(b)) a will be inserted in the list b in ordered manner
# use ord() to get ascii value of any char
# reversed(list) returns reversed list
# compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
# condition_is_true if condition else condition_is_false   # acts like ? operator in C
import functools
import io
import itertools

fin = None


def inMajority(x):
    n = functools.reduce(lambda x,y: x + y, x)
    for i in range(len(x)):
        if x[i] > n//2:
            return True, i
    return False, None


def isZero(x):
    n = functools.reduce(lambda x,y: x + y, x)
    if n == 0:
        return True
    return False


# solve question here.
def solve():
    D = {}
    flag = 0
    left_list=[]
    n = num()
    senetors = nums()
    for i in range(n):
        D[chr(65+i)] = senetors[i]

    left = permutations(''.join(str(x) for x in range(n)))
    left_alone = range(n)
    check = 1
    print(left)
    while not isZero(senetors) or flag != 1:
        temp = senetors
        if temp == senetors:
            for j in reversed(left_alone):
                while check == 1:
                    senetors[j] -= 1
                    major, party = inMajority(senetors)
                    if major:
                        senetors[j] += 1
                        check = 0
                    else:
                        left_list.append(chr(j+65))
                        check = 1

            if isZero(senetors):
                flag = 1
                break
        if flag == 1:
            break
        for j in range(len(left)):
            print(senetors)
            for k in range(2):
                senetors[int(left[j][k])] -= 1

            major, party = inMajority(senetors)
            if major:
                for k in range(2):
                    senetors[int(left[j][k])] += 1
            else:
                left_list.append(chr(int(left[j][0])+65) + chr(int(left[j][1])+65))
            if isZero(senetors):
                flag = 1
                break
        if flag == 1:
            break

    print(left_list)
    s = ' '.join(left_list)
    return s

    #for i in range(n):
        #senetors[i]
    #major, party = inMajority(senetors)

    #print(major)
    #print(party)
    #print(n)
    #print(senetors)
    #print(D)


def main():
    fname = "test.in"
    global fin
    fin = io.open(fname)
    fout = io.open(fname+'.out', 'w')

    t = int(fin.readline())

    for i in range(t):
        fout.write('Case #%d: ' % (i + 1))
        fout.write('%s\n' % str(solve()))

    fin.close()
    fout.close()


def nums():
    return [int(x) for x in fin.readline().split()]


def fnums():
    return [float(x) for x in fin.readline().split()]


def num():
    return int(fin.readline())


def sstrip():
    return fin.readline().strip()


def strs():
    return fin.readline().split()


def arrstr(a, sep=' '):
    return sep.join([str(x) for x in a])


def permutations(s, duplicate=False):
    perms = [''.join(p) for p in itertools.permutations(s, )]
    if not duplicate:
        perms = list(set(perms))
    return perms
    # return [''.join(p) for p in itertools.permutations(s, )]


def combinations(s, repeat=2):
    perms = [''.join(p) for p in itertools.product(str(s), repeat=repeat)]
    return perms
    # return [''.join(p) for p in itertools.permutations(s, )]


if __name__ == '__main__':
    main()
