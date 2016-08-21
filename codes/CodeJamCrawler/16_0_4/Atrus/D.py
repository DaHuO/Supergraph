def calc_c(pos, K, C): #Note we handle the final offset ourselves to skip better
    if(C == 1): return 0
    current = pos * K**(C-1)
    return current + calc_c(pos, K, C-1)

def solve(K, C, S):
    #note, K,C,S aren't indexed at 0
    index = []
    k_pos = 0
    c_pos = 0
    for i in range(S):
        while c_pos <= k_pos and c_pos+1 < K and C != 1:
            c_pos+=1
        #if(k_pos == c_pos and C > 1):
            #k_pos+=1

        index.append(calc_c(c_pos, K, C) + k_pos+1)
        #index.append(c_pos * K**(C-1) + k_pos+1)

        if c_pos > k_pos:
            k_pos = c_pos + 1
        else:
            k_pos +=1

        if k_pos >= K:
            index_str = map(str, index)
            return " ".join(index_str) #solved early

    return "IMPOSSIBLE"

if __name__ == "__main__":
    testcases = eval(input())
    for case_num in range(1, testcases+1):
        data = str(input()).split(" ")
        K = int(data[0])
        C = int(data[1])
        S = int(data[2])
        print("Case #%i: %s" % (case_num, solve(K,C,S)))
