#!/usr/bin/python3
import sys

T = int(input())
numbers = list(map(int, sys.stdin.readlines()))

def Reduce(N):
    tmp = str(N)
    if len(tmp) <= 2:
        return N
    if len(tmp) >= 3:
        last1 = tmp[-1:]
        if tmp[-2] == last1 and tmp[-3] == last1 and last1 != '8':
            tmp = str(Reduce(int(tmp[:-1])))
    if len(tmp) >= 6:
        last2 = tmp[-2:]
        if tmp[-4:-2] == last2 and tmp[-6:-4] == last2 and last2 != '88':
            tmp = str(Reduce(int(tmp[:-2])))
    return int(tmp)

def BruteForce(N, verbose=False):
    todo = '0123456789'
    i = 0
    while len(todo) > 0:
        i += 1
        for e in str(i*N):
            if e in todo:
                todo = todo.replace(e,'')
        if verbose:
            print(i, N, i*N, todo)
        if i > 2000000:
            print('WARNING! BREAK', N)
            break
    return todo, i

test = False
verbose = False
for i in range(T):
    N_new = Reduce(numbers[i])
    if numbers[i] > 0:
        todo, counter = BruteForce(N_new, verbose=verbose)
        if test and N_new != numbers[i]:
            todo_test, counter_test = BruteForce(numbers[i], verbose=verbose)
            if counter != counter_test:
                print('ERROR: N N_new, counter, counter_new', numbers[i], N_new, counter, counter_test)
            # else:
            #     print('WORKS: N N_new, counter, counter_new', numbers[i], N_new, counter, counter_test)
    else:
        todo = '123456789'
    if not test:
        if len(todo) > 0:
            print("Case #{}: {}".format(i+1, 'INSOMNIA'))
        else:
            print("Case #{}: {}".format(i+1, counter*numbers[i]))



    
