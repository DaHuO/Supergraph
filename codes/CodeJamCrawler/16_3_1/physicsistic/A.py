import sys
import itertools


def senator(i):
    return chr(ord('A')+i)


def solve(N,P):
    answer = ''
    while True:
        S = sum(P)
        if S == 0:
            break
        a = ''
        found = False

        for i, j in itertools.product(range(N), repeat=2):
            new_H = (S-2)/2+1
            if i == j:
                # check that there are at least 2 senator i remaining
                if P[i] > 1:
                    if all(P[n] < new_H if n != i else P[n] - 2 < new_H for n in range(N)):
                        found = True
                        a += senator(i) + senator(j)
                        P[i] -= 1
                        P[j] -= 1
                        break
            else:
                if P[i] > 0 and P[j] > 0:
                    if all(P[n] < new_H if n not in [i,j] else P[n] - 1 < new_H for n in range(N)):
                        found = True
                        a += senator(i) + senator(j)
                        P[i] -= 1
                        P[j] -= 1
                        break
        if not found:
            for i in range(N):
                new_H = (S-1)/2+1
                if P[i] > 0:
                    if all(P[n] < new_H if n != i else P[n] - 1 < new_H for n in range(N)):
                        found = True
                        a += senator(i)
                        P[i] -= 1
                        break
        answer += a + ' '
    return answer

 
def io(filename):
    output = open(filename.split('.')[0]+'.out', 'w')
    with open(filename, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            N = int(f.readline().rstrip('\n'))
            P = map(int,f.readline().rstrip('\n').split())
            string = "Case #{n}: {y}".format(n=t+1, y=solve(N,P))
            print string
            print "======================================================="
            output.writelines(string+'\n')   
 
if __name__ == '__main__':
    input_file = sys.argv[1]
    io(input_file)