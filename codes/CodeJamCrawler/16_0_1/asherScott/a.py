import sys

complete = [0,1,2,3,4,5,6,7,8,9]

f_in = open(sys.argv[1], 'r')
f_out = open(sys.argv[2], 'a')

T = int(f_in.readline().strip())


for i in range(T):
    seen_N = []
    last_N = 0
    c = 1 
    
    case = int(f_in.readline().strip())

    if case == 0:
        f_out.write("Case #{}: INSOMNIA\n".format(i+1))
        
    else:
        while complete != sorted(seen_N):
            last_N = case * c
            for j in range(len(str(last_N))):
                if int(str(last_N)[j]) not in seen_N:
                    seen_N.append(int(str(last_N)[j]))
            c += 1
        f_out.write("Case #{}: {}\n".format(i+1, last_N))
