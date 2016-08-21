def gold(start,comp,stud):
    if (stud < int((start+1)/2)):
        return "IMPOSSIBLE"
    if (comp == 1 or start == 1):
        if(stud < start):
            return "IMPOSSIBLE"
        else:
            ans = []
            for i in range(1,start+1):
                ans += [i]
            return ans
    s = []
    for i in range(0,int((start+1)/2)):
        num = pow(start,comp-1)
        s += [min(num*(2*i) + 2*(i+1),num*start)]
    return s

def test():
    t = int(input())
    out = [0]*t
    for i in range(0,t):
        case = input().split()
        print(int(case[0]))
    
def main():
    t = int(input())
    out = [0]*t
    for i in range(0,t):
        case = input().split()
        out[i] = gold(int(case[0]),int(case[1]),int(case[2]))

    for i in range(0,len(out)):
        temp = ''
        for val in out[i]:
            temp += str(val) + " "
        print("Case #" + str(i + 1) + ": " + str(temp))
    
