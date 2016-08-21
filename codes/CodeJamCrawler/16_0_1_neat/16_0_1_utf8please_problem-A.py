#!/usr/bin/env python3

def solve(fin, fout):
    n = int(fin.readline())
    if not n:
        fout.write('INSOMNIA\n');
        return
    nums = set()
    cur = n;
    while True:
        nums.update(set(str(cur)))
        if len(nums) == 10:
            break
        cur += n

    fout.write(str(cur));
    fout.write('\n');
