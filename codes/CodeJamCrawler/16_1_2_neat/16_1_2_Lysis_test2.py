import collections
cases = int(input())
def list_to_str(ls):
    r = ""
    for l in ls:
        r += str(l)
        r += " "
    return r
for i in range(cases):
    N = int(input())
    result = collections.defaultdict(lambda:0)
    heights = set()
    all_papers = [list(input().split(" ")) for i in range(2*N -1)]
    for paper in all_papers:
        for num in paper:
            result[num]+=1
            heights.add(num)
    lonely = []
    for h in heights:
        if result[h] % 2 == 1:
            lonely.append(int(h))
    print("Case #{}: {}".format(i+1, list_to_str(sorted(lonely))))
