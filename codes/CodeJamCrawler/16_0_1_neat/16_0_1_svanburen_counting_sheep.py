#!/usr/bin/python


def main():
    with open("input.txt") as f:
        inputs = [line.strip() for line in f]
        del inputs[0]
        check = set()
        for z in range(10):
            check.add(z)
        for i, x in enumerate(inputs):
            val = int(x)
            if val == 0:
                print("Case #{}: INSOMNIA".format(i + 1))
                continue
            cur = set([int(l) for l in x])
            #print("CUR: {}".format(cur))
            #print("CHECK: {}".format(check))
            j = 1
            while cur != check:
                j += 1
                cur_val = val * j
                #print(cur_val)
                for l in str(cur_val):
                    cur.add(int(l))
                #print("CUR: {}".format(cur))
            print("Case #{}: {}".format(i + 1, val * j))

main()
