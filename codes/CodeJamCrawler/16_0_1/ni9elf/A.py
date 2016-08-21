'''
Created on 09-Apr-2016

@author: nigel
'''


def count_sheep(n):
    if(n == 0):
        return "INSOMNIA"
    i = 1
    digit_set = set()
    while(True):
        n1 = i * n
        i += 1
        print n1
        digit_list = [int(x) for x in str(n1)]
        print digit_list
        digit_set = digit_set.union(set(digit_list))
        if(len(digit_set) == 10):
            return n1   


if __name__ == '__main__':
    f1 = open('a_large_input.in', 'r')
    f2 = open('a_large_output.in', 'w')
    t = int(f1.readline())
    for i in range(t):
        n = int(f1.readline().rstrip())
        f2.write("Case #{}: {}\n".format(i + 1, count_sheep(n)))
    f1.close()
    f2.close()