import sys

T = int(raw_input())

for t in range(1, T+1):
    N,R,P,S = map(int, raw_input().split())

    ret = 'IMPOSSIBLE'

    orders = []

    for winner in ['S', 'R', 'P']:
        order = winner

        for i in range(N, 0, -1):
            order_new = ''
            for c in order:
                if c == 'S':
                    if i >= 3:
                        order_new += 'SP'
                    else:
                        order_new += 'PS'
                elif c == 'P':
                    order_new += 'PR'
                else: # c == 'R'
                    if i == 1: 
                        order_new += 'RS'
                    else: 
                        order_new += 'SR'
            order = order_new

        cnts = map(lambda x: order.count(x), ['R','P','S'])
        if cnts == [R,P,S]:
            orders.append(order)
        #print orders

    if orders:
        sorted(orders)
        ret = orders[0]

    print 'Case #%d: %s' % (t, ret)
