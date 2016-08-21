#!/usr/bin/env python3
def str_list(n):
    str_n = str(n)
    list = []
    for i in str_n:
        list.append(int(i))
    return list

def add_to_list(saw_list, new_list):
    saw_list_set = set(saw_list)
    new_list_set = set(new_list)
    result = saw_list + list(new_list_set - saw_list_set)
    return sorted(result)

def counting_sheep(n):
    saw_list = []
    i = 1
    last_result = None
    while True:
        result = i * n;
        if last_result == result:
            return None
        new_list = str_list(result)
        saw_list = add_to_list(saw_list, new_list)
        if saw_list == list_result:
            return result
        i = i + 1 
        last_result = result
        


def main():
    list_n = []
    T = int(input())
    for i in range(0, T):
        n = int(input())
        list_n.append(n)
    i = 1
    for n in list_n:
        res = counting_sheep(n)
        if res is None:
            print('Case #{0}: INSOMNIA'.format(i))
        else:
            print('Case #{0}: {1}'.format(i,res))
        i = i + 1


if __name__ == '__main__':
    list_result = list(range(0,10))
    main()