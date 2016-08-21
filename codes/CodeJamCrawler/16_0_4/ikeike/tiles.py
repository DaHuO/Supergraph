import sys

stream = sys.stdin

os = sys.stdout

T = int(stream.readline().strip())

for i in range(T):
    k, c, s = stream.readline().split()
    k, c, s = int(k), int(c), int(s)
    os.write('Case #'+str(i+1)+': ')
    for i in range(k):
        os.write(str(i+1)+' ')
    os.write('\n')
