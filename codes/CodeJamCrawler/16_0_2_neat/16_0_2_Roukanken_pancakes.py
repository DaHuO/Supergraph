import itertools

def work():
    data = reversed(input().strip() + "+")
    return len([x for x in itertools.groupby(data)]) - 1


T = int(input())
for test_case in range(T):
    print ("Case #{}:".format(test_case+1), work())