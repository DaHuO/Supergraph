
def counting_sheep(num):
    # import ipdb; ipdb.set_trace()
    if num == 0:
        return 'INSOMNIA'

    remains = set([str(idx) for idx in range(0, 10)])
    curr = num
    while True:
        [remains.discard(ch) for ch in str(curr)]
        if not remains:
            return curr
        curr += num

cases = input()

for idx in range(int(cases)):
    num = int(input())
    print("Case #{}: {}".format(
        idx+1,
        counting_sheep(num
        )))
