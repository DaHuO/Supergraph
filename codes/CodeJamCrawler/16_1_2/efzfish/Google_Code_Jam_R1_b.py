
# coding: utf-8



from collections import Counter



T = int(raw_input())
#data = []
flat_data = []
for k in range(T):
    #data0 = []
    N = int(raw_input())
    flat_data0 = []
    for i in range(2*N-1):
        row = map(int, raw_input().split(' '))
        #data0.append(row)
        flat_data0 = flat_data0 + row
    flat_data.append(flat_data0)



def pro_b(x):
    ct = Counter(x)
    y = []
    for i in ct:
        if ct[i] & 1:
            y.append(i)
    return y


for k in range(T):
    answer = sorted(pro_b(Counter(flat_data[k])))
    print 'Case #{}: {}'.format(k+1, str(answer)[1:-1].replace(',',''))





