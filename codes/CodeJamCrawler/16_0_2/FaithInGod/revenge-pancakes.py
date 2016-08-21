"""Problem B. Revenge of the Pancakes"""
with open("B-small-attempt0.in") as f:
    out = open("out-revenge-pancakes.in","w")
    T = int(f.readline())
    
    for i in range(1, T + 1):
        counter = 0
        N = list(f.readline().strip())
        if len(N) == 1:
            if N == ['-']:
                counter = 1
            elif N == ['+']:
                counter = 0
        elif len(N) > 1:
            if all(x == '+' for x in N):
                counter = 0
            elif all(x == '-' for x in N):
                counter = 1
            else:
               while not all(x == '+' for x in N):
                    if N.pop() == '-':
                        N = ['+' if x == '-' else '-' for x in N]
                        counter += 1
                    j = len(N) - N[-1::-1].index('-') -1
                    L = N[:j:-1]
                    F = N[:j + 1]
                    N = ['+' if x == '-' else '-' for x in F] + list(reversed(L))
                    counter += 1
        out.write("Case #{}: {}".format(i, counter) + ("\n","")[i == T])
        #print("Case #{}: {}".format(i, counter))
    out.close()
print("done")