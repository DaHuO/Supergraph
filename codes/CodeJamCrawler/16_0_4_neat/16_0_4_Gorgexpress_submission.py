out = open("A.out", "w")
with open("A.in") as f:
    f.next()
    T = 1
    for line in f:
        K, C, S = (int(num) for num in line.split())
        indices = []
        if S * C < K:
            out.write("Case #{}: IMPOSSIBLE\n".format(T))
        else:
            if C == 1 or K == 1:
                for i in range(1, K + 1):
                    indices.append(i)
            else:
                if C > K:
                    for i in range(1, K + 1):
                        indices.append(i)
                else:
                    for i in range(0, K, C):
                        index = i
                        for j in range(1, C):
                            if K - i < C and j >= K - i:
                                index = (index * K) + i
                            else:
                                index = (index * K) + (1 * j) + i
                        indices.append(index + 1)
            out.write("Case #{}: {}\n".format(T, " ".join(str(idx) for idx in indices)))
        T += 1
        
        
        
        
            
out.close()