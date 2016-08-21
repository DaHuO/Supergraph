
def count(pancakes):
    num = 0
    last_seen = '+'
    for pancake in pancakes[::-1]:
        if pancake != last_seen:
            num += 1
        last_seen = pancake
    return num


if __name__ == '__main__':
    f = open("B-large.in", 'r')
    r = open("result.txt", 'w')
    test = int(f.readline())
    for i in range(test):
        pancakes = f.readline().strip('\n')
        result = count(pancakes)
        r.write('Case #%s: %s' %(i+1,result))
        if i != test-1:
            r.write('\n')
    r.close()
    f.close()