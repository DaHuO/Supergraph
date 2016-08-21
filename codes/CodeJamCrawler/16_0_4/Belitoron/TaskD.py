fi = open('D:\D-small-attempt0.in', 'r')
fo = open('D:\output.txt', 'w')

z = int(fi.readline())
for i in range(1, z+1):
    K, C, S = map(int, fi.readline().strip().split())
    fo.write("Case #{0}: {1}\n".format(i, ' '.join((str(i) for i in range(1, S+1)))))
