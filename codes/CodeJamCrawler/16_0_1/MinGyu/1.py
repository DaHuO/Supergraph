import array

check_num = range(10)

def check_set(s):
    for i in check_num:
        if i not in s:
            return False

    return True

def main():
    tcase = input()

    for t in xrange(tcase):

        N = input()
        S = set()
        cnt = 1
        if N == 0:
            print 'Case #%d:'%(t+1), 'INSOMNIA'
            continue

        while check_set(S) == False:
            curr = cnt*N
            while curr > 0:
                S.add(curr%10)
                curr/=10
            cnt += 1

        print 'Case #%d:'%(t+1), (cnt-1)*N



if __name__ == '__main__':
    main()
