import sys
from sets import Set


def count(num):
    """ Count digits in 1N, 2N, 3N,... until all 10 digits (0-9) appear """
    s = Set()
    counter = 1
    while True:
        for c in str(counter * num):
            s.add(c)
        if len(s) == 10:
            return counter * num
        elif counter > 2000000:
            return -1
        else:
            counter += 1
    return counter * num
                
def main():
    in_file = open('sheep_in.txt', 'r')
    out_file = open('sheep_out.txt', 'w')
    list = []
    try:
        for line in in_file:
            print(line)
            list.append(int(line.strip()))
    except:
        pass
    in_file.close()
    
    for x in range(1, list[0] + 1):
        r = count(list[x])
        out_file.write('Case #' + str(x) + ': ' + (str(r) if r != -1 else 'INSOMNIA') +'\n')
    out_file.close()

if __name__ == '__main__':
    main()