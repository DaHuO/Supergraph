for i in range(1, int(input()) +1):
    # print('Case', '#'+str(i))
    num = int(input())
    ind = 1
    off = 0
    seen = [0]*10
    while sum(seen) < 10:
        if ind > 10000:
            print('Case', '#'+str(i)+':', 'INSOMNIA')
            break
        nn = num * ind
        seen[nn % 10] = 1
        nn = int(nn / 10)
        off += 1
        while nn > 0:
            seen[nn % 10] = 1
            nn = int(nn / 10)
            off += 1
        ind += 1
    if sum(seen) is 10:
        print('Case', '#'+str(i)+':', num * (ind-1))
