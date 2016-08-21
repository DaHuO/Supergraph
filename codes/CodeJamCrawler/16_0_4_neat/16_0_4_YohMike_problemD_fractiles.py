import os
import sys
import itertools

def output_format(answer,test_case):
    output = "Case #%d:" % (test_case+1)
    if answer == "IMPOSSIBLE":
        output += " %s" % str(answer)
    else:
        for tile in answer:
            output +=" %d" % tile
    output +="\n"
    return output
def interpret_in_base(binary_number,base =2):
    digits = str(binary_number)
    number = 0
    for i in range(len(digits)):
        number += (base ** i )*int(digits[len(digits)-i-1])
    return number

# def generate_all_perms(K):
#     d = {}
#     for j in range(K+1):
#         sequence = '0'*j +'1'*(K-j)
#         for i in list(itertools.permutations(sequence,len(sequence))):
#             d["".join(i)] = d.get("".join(i),0)+1
#     return d.keys()

# def generate_fractile(pattern,complexity):
#     fractile = pattern
#     for i in range(complexity-1):
#         aux = ""
#         for f in fractile:
#             if f == '1':
#                 aux += pattern
#             else:
#                 aux += "0"*len(pattern)
#         fractile = aux
#     return fractile
    
# def get_indices_from_fractiles(fractiles):
#     indices = [0 for i in fractiles[0]]
#     for fractile in fractiles:
#         for i,f in enumerate(fractile):
#             indices[i] += int(f)
#     return indices

if __name__ == "__main__":
    #f = open("A-small-practice.in",'r')
    f = open("D-small-attempt1.in",'r')
    test_cases = int(f.readline())
    out = open("results_D_1.txt",'w')

    
    

    print test_cases
    for i in range(test_cases):
        print "\nTest case #%d"%i
        K, C, S = f.readline().strip("\n").split(" ")
        print K, C, S
        K = int(K)
        C = int(C)
        S = int(S)
        print K**C
        if C == 1:
            if S < K:
                answer = "IMPOSSIBLE"
            else:
                answer = [l for l in range(1,int(S)+1)]
        else:
            if S == K:
                #go through the first S indices to see a valid permutation
                answer = [l for l in range(1,S+1)]
            else:
                #pick the last before K
                answer = [i*(K-1) for i in range(K,K**C,K)]
                answer = answer[:S]

            # d = generate_all_perms(int(K))
            # print "#perms: %d" %len(d)
            # fractiles = []
            # print d
            # for m in range(len(d)):        
            #     #print d[i]
            #     fractiles.append(generate_fractile(d[m],int(C)))
            # print fractiles
            # indices = get_indices_from_fractiles(fractiles)
            # print indices
            # if int(S) < min(indices):
            #     answer = "IMPOSSIBLE"
            # else:
            #     answer = []
            #     print indices
            #     for index in range(int(S)):
            #         min_index = indices.index(min(indices))
            #         answer.append(min_index+1)
            #         indices[min_index] = max(indices)+1
        print answer
        output = output_format(answer,i)
        out.write(output)

