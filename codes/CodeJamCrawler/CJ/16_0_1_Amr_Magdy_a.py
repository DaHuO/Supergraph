T = int(raw_input())
n_array = []
for case in range(T):
    N = int(raw_input())
    n_array.append(N)

result = {}
for i in range(max(n_array)+1):
    try_it = 80
    digits = set()
    counter = 0
    while try_it:
        counter+= 1
        try_it-=1
        for char in str(i*counter):
            digits.add(char)
        if len(digits) == 10:break
    if len(digits) == 10:
        result[i] = i*counter
    else:
        result[i] = "INSOMNIA"

for case, N in enumerate(n_array):
    print "Case #{}: {}".format(case+1, result[N])