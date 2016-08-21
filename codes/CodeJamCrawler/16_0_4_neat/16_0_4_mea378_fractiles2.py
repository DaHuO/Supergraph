if __name__ == '__main__':
    input = 'D-small-attempt0.in'
    output = 'D-small-attempt0.out'

    with open(input) as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content]

    with open(output, 'w') as o:
        for i, c in enumerate(content[1:]):
            k, c, s = c.split(' ')

            o.write("Case #%d: %s" % (i+1, ' '.join(str(x+1) for x in range(int(s))) ))
            o.write('\n')
