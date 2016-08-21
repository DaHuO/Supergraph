

def run(N):
    if N == 0:
        return None
    needs = set('0123456789')
    now = N
    while True:
        needs -= set(str(now))
        if not needs:
            return now
        now += N
        

if __name__ == '__main__':
    for t in range(int(input())):
        result = run(int(input()))
        print('Case #{}: {}'.format(t + 1, result if result else 'INSOMNIA'))
                       
