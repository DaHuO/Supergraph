from read import read
from Euler import primecheck
import threading
import multiprocessing
from multiprocessing.managers import SyncManager
from math import sqrt


def inc_bin(num):
    return bin(int(num, 2) + int('110', 2))[2:]


def add_bin(num, anum):
    return bin(int(num, 2) + int(anum, 2))[2:]


def first_divisor(num, start=1):
    if num>2 and num%2 == 0:
        return 2
    if num>3 and num%3 == 0:
        return 3
    i = start*6
    sqnum = sqrt(num)
    while i+1 <= sqnum:
        if num%(i-1) == 0:
            return i-1
        if num%(i+1) == 0:
            return i+1
        i+=6
        if i>200000:
            return False
    return False


def calc(dig, start):
    ret = [start]
    s = start
    while True:
        for i in range(2, 11):
            # print(i, end='')
            # print(ret)
            tmp = first_divisor(int(s, i))
            if tmp:
                ret.append(tmp)
                continue
        if len(ret) == 10:
            # print(ret)
            return ret, s
        s = inc_bin(s)
        ret = [s]


anss = []
manager = SyncManager()
manager.start()
ls = manager.list()

def calc_and_write(filepath, dig, start, end, l, t_cnt):
    current_val = start
    for _ in range(t_cnt):
        ans, current_val = calc(dig, start=current_val)
        current_val = inc_bin(current_val)
        # with open(filepath, 'a') as outfile:
        #     # outfile.write('{}\n'.format(' '.join(map(str, ans))))
        #     anss.append('{}\n'.format(' '.join(map(str, ans))))
        #     print('{}'.format(' '.join(map(str, ans))))
        # outfile.write('{}\n'.format(' '.join(map(str, ans))))
        l.append('{}\n'.format(' '.join(map(str, ans))))
        # anss.append('{}\n'.format(' '.join(map(str, ans))))
        print('{}'.format(' '.join(map(str, ans))))




def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    T = int(it())

    num_of_digits, num_of_case = map(int, it().split())
    start = '1'+'0'*(num_of_digits-2)+'1'
    threads = []
    processes = []
    num_of_process = 4
    for _ in range(num_of_process):
        # threads.append(threading.Thread(target=calc_and_write, kwargs={'filepath':outfilename, 'dig':num_of_digits, 'start': start, 'end': add_bin(start, '1'+'0'*10)}))
        # threads[-1].start()
        processes.append(multiprocessing.Process(target=calc_and_write, kwargs={'filepath':outfilename, 'dig':num_of_digits, 'start': start, 'end': add_bin(start, '1'+'0'*10), 'l':ls, 't_cnt':num_of_case//num_of_process}))
        processes[-1].start()
        start = add_bin(start, '1'+'0'*20)
    # for t in threads:
        # t.join()
    for p in processes:
        p.join()
    # print(anss)
    with open(outfilename, 'w') as outfile:
        outfile.write('Case #1:\n')
        print('Case #1:')
        # for line in anss:
        for line in ls:
            print(line.strip())
            outfile.write(line)




if __name__ == '__main__':
    main()
