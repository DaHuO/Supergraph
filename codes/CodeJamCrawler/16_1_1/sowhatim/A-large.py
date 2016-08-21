#!/usr/bin/env python3
cases = int(input())
for case in range(1,cases+1):
    inpt = [s for s in input()]
    result = []
    result.append(inpt[0])
    for i in inpt[1:]:
        if ord(i) >= ord(result[0]):
            result.insert(0,i)
        else:
            result.append(i)
    print ("Case #{}: {}".format(case,''.join(result)))
