import sys
from bitarray import bitarray

i = 1
bit_array = bitarray(10)


def TestBits():
    global bit_array
    for j in range(0, 10):
        if not bit_array[j]:
            return False
    return True


def TestLine(x):
    xx = int(x)
    if xx == 0:
        return 'INSOMNIA'
    global i, bit_array
    i += 1
    ii = 1
    nn = 1

    while not TestBits():
        nn = xx * ii
        s_nn = str(nn)
        for s in s_nn:
            bit_array[int(s)] = True
            # print xx,ii,nn,bit_array
        ii += 1
    return s_nn


f = open('test.tst')
tests_count = f.readline()
while True:
    s = f.readline()
    if s == '':
        break
    bit_array.setall(0)
    r = TestLine(s)
    print 'Case #%d: %s' % (i, r)



# s = int(f.readline())




