__author__ = 'radykov'
def sort_ps(Ps):
    return sorted(Ps, key=lambda k: k[1])

def sum(Ps):
    sum = 0
    for i in range(len(Ps)):
        sum += Ps[i][1]
    return sum

def solve(Ps):
    p_remaining = sum(Ps)
    N = len(Ps)
    answer = ""
    while (p_remaining > 0):
        # print Ps
        if Ps[N-1][1] > Ps[N-2][1] + 1:
            answer += Ps[N-1][0] + Ps[N-1][0] + " "
            Ps[N-1][1] -= 2
            p_remaining -= 2
        elif Ps[N-1][1] == Ps[N-2][1] and p_remaining != 3:
            answer += Ps[N-1][0]
            answer += Ps[N-2][0] + " "
            Ps[N-1][1] -= 1
            Ps[N-2][1] -= 1
            p_remaining -= 2
        else:
            answer += Ps[N-1][0] + " "
            Ps[N-1][1] -= 1
            p_remaining -= 1
        Ps = sort_ps(Ps)
    return answer[0: len(answer)-1]


data = open('input_a_example', 'r').read().split('\n')
out = open('A_large', 'w')
T = int(data[0])
index = 1
for i in range(1, T*2, 2):
    N = data[i]
    Ps_raw = data[i + 1].split(' ')
    Ps_labelled = []
    for i in range(len(Ps_raw)):
        c = unichr(65+i)
        Ps_labelled.append([c, int(Ps_raw[i])])
    out.write("Case #" + str(index) + ": " + solve(sort_ps(Ps_labelled)) + '\n')
    index +=1
out.close()

