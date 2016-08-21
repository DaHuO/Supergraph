#!/usr/bin/python3

Rounds = int(input());
for r in range(Rounds):
    N = int(input())
    number_bag = set(str(N))
    for i in range(1,200):
        number_bag |= set(str(i*N))
#        print(i, number_bag, len(number_bag))
        if len(number_bag) >= 10:
            print("Case #{}: {}".format(r+1, i*N))
            break
    else:
        print("Case #{}: INSOMNIA".format(r+1))

