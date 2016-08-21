cases = int(raw_input())

for case in range(cases):
    k, c, s = (int(st) for st in raw_input().split())

    r = range(1, k + 1)

    print('Case #' + str(case + 1) + ': ' + str(r).strip('[]').replace(',', ''))
