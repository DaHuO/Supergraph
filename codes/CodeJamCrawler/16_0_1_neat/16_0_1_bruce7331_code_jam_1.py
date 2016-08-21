#! /usr/bin/python3

class Problem:
    def __init__(self, nb_inputs):
        self.inputs = nb_inputs
        self.tests = [0] * nb_inputs

def parse():
    nb_inputs = int(input())
    a = Problem(nb_inputs)
    for i in range(nb_inputs):
        a.tests[i] = int(input())
    return a

def solve():
    input_set = parse()
    for i in range(input_set.inputs):
        tmp = input_set.tests[i]
        arr = [False]*10
        for z in range(1, 10000):
            for indice in str(tmp*z):
                arr[int(indice)] = True
            if arr == [True]*10:
                print("Case #{}: {}".format(i + 1, tmp*z))
                break
        if z == 9999:
            print("Case #{}: INSOMNIA".format(1))

if __name__ == '__main__':
    solve()
