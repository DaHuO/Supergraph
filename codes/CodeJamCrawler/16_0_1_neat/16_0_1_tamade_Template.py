import collections

with open('A-large-practice.in', 'r') as f:
    data = f.read()

data = data.split('\n')
output = []

print(data.pop(0), 'cases.')

dirx = collections.defaultdict()
while data:
    dirx.clear()
    if data[0] == '':
        break
    n, m = map(int, data.pop(0).split(' '))
    for i in range(n):
        dirstr = data.pop(0).split('/')[1:]
        curr = dirx
        for ele in dirstr:
            curr = curr.setdefault(ele, collections.defaultdict())
    count = 0
    for i in range(m):
        dirstr = data.pop(0).split('/')[1:]
        curr = dirx
        for ele in dirstr:
            if ele not in curr:
                curr.setdefault(ele, collections.defaultdict())
                count += 1
            curr = curr.get(ele)
    output.append(count)

with open('submission.txt', 'w+') as f:
    i = -1
    for i, answer in enumerate(output):
        f.write("Case #%i: %s\n" % (i+1, answer))
        print("Case #%i: %s" % (i+1, answer))
    print('\n%i cases written to file' % (i+1))
