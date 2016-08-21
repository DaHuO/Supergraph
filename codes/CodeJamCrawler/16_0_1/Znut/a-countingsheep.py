tmp = 0

def set_seen(num):
    global tmp 
    tmp |= 1 << (num % 10)
    if num >= 10:
        set_seen(num/10)

def main(num):
    if num == 0:
        return 0
    i = 1
    while(True):
        curr = i*num
        set_seen(curr)
        if tmp & 0x3ff == 0x3ff:
            return curr
        i += 1

if __name__ == '__main__':
    for t in range(input()):
        answer = main(input())
        print 'Case #%d:'%(t+1),
        print answer if answer > 0 else 'INSOMNIA'
        tmp = 0
