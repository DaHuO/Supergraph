T = int(input())

def compare(s_1, s_2):
    res = True
    for i in range(len(s_1)):
        if s_1[i] != '?' and s_1[i] != s_2[i]:
            res = False 
    return res

for i in range(T):
    c, j = input().split()
    
    all_c = []
    all_j = []
    
    for k in range(10 ** len(c)):
        s_k = str(k)
        s_k = '0' * (len(c) - len(s_k)) + s_k
        if compare(c, s_k):
            all_c.append(s_k)
        if compare(j, s_k):
            all_j.append(s_k)

    
    minimals = [(all_c[0], all_j[0])]
    m = abs(int(all_c[0]) - int(all_j[0]))
    for c_i in all_c:
        for j_i in all_j:
            if abs(int(c_i) - int(j_i)) < m:
                minimals = [(c_i, j_i)]
                m = abs(int(c_i) - int(j_i))
            elif abs(int(c_i) - int(j_i)) == m:
                minimals.append((c_i, j_i))
    
    minimals.sort()
    print('Case #' + str(i + 1) + ': ' + minimals[0][0] + ' ' + minimals[0][1])
    
                    