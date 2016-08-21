def work():
    K, C, S = [int(x) for x in input().strip().split()]
    return " ".join([str(x) for x in range(1, S+1)])

T = int(input())
for test_case in range(T):
    print ("Case #{}:".format(test_case+1), work())