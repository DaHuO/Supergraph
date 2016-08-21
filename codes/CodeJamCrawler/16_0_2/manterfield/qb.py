from itertools import groupby


def readint(): return int(raw_input())

T = readint()
for t in range(T):
    bits = raw_input().rstrip('+')
    bit_blocks = ''.join(i[0] for i in groupby(bits))
    bit_len = len(bit_blocks)

    if bit_len == 0:
        answer = 0
    else:
        last_bit = True if bit_blocks[0] == "+" else False
        answer = bit_len - 1 if last_bit and bit_len % 2 == 1 else bit_len

    print "Case #%d: %d" % (t+1, answer)
