def solve(s):

    s = list(s)
    lenS = len(s)

    it = 0
    while True:

        same = 0
        for j in range(1, lenS):
            if( s[j-1] != s[j]):
                break
            else:
                same = j

        if same == lenS-1:
            if s[0] == '-':
                return it+1
            else:
                return it

        s[0:same+1] = ['-' if x=='+' else '+' for x in s[same:None:-1]]
        it += 1

for i,_ in enumerate(range(int(input()))):
    print('Case #{}: {}'.format(i+1, solve(input())))
