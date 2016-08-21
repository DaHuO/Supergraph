#!/usr/bin/env python3
import sys
from code_jam import CodeJam

def solve(i, data):
    # print(data)
    if len(data) == 1:
        return data[0]

    payload = data[0]
    data = data[1:]

    last = payload
    for i, x in enumerate(data):
        if x >= last and x >= payload[0]:
            payload = x + payload
        else:
            payload = payload + x

        last = x

    return payload

if __name__ == "__main__":
    cj = CodeJam(sys.argv)
    test_cases, data = cj.run()

    for i in range(0, test_cases):
        tries = solve(i, [x for x in data[i]])
        cj.print_output(i+1, tries)
