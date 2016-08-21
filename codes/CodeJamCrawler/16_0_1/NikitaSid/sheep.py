import pickle

digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

result = {}

for N in range(0, 1000001):
    if N == 0:
#            print('0' + ',' + 'INSOMNIA', file=f)
        result[0] = 'INSOMNIA'
        continue

    seen = set()

    factor_by = 1

    while seen != digits:
        factorized = N*factor_by
        seen = seen | {int(i) for i in str(factorized)}
        factor_by += 1

#        print(str(N) + ',' + str(factorized), file=f)
    result[N] = factorized

with open('cache.out', mode='wb') as f:
    pickle.dump(result, f)