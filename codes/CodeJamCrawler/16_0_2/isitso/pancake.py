from sys import argv


def flip_helper(xs, l):
    i = len(xs) - 1
    result = 0
    while i > 0 and xs[i] == xs[i - 1]:
        i -= 1
        
    if i == 0:
        return (1, ''.join(['+' if x == '-' else '-' for x in xs[::-1]]))
    else:
        print('sending to next recursive ' + xs[:i])
        result, ys = flip_helper(xs[:i], l)
        print('got back ' + ys + ' ' + str(result))
        xs = ys + xs[i:]
        if len(xs) != l or (len(xs) == l and xs.find('-') != -1):
            return (result + 1, ''.join(['+' if x == '-' else '-' for x in xs[::-1]]))
        return (result, xs)

def flip(xs):
    """ Flip the cakes so that it return all '+++' """
    count = 0
    if xs.find('-') != -1:
        count, xs = flip_helper(xs, len(xs))
    return (count, xs)

    
    


def main():
    script, filename = argv
    in_file = open(filename, 'r')
    out_file = open(filename.split('.')[0] + '.out', 'w')
    list = []
    try:
        for line in in_file:
            print(line)
            list.append(line.strip())
    except:
        pass
    in_file.close()
    
    for x in range(1, int(list[0]) + 1):
        count, _ = flip(list[x])
        print('Case #' + str(x) + ': ' + str(count) + ' ' + ''.join(_))
        out_file.write('Case #' + str(x) + ': ' + str(count) + '\n')
    out_file.close()

if __name__ == '__main__':
    main()