def get_rep(n, b):
    rep = 0
    for i in range(0,len(n)):
        rep = rep + n[len(n)-1-i]*b**i
    return rep

def is_prime(n):
    div = 2

    while(div*div <= n):
        if(n % div == 0):
            return [False, div]
        div = div + 1

        if div > 10**6:
            return [True, div]

    return [True, div]


def expand_string(s, M):
    while(len(s) < M):
        s = "0" + s
    return s


N = 32
J = 500
M = N - 2
max_bin = [1 for i in range(M)]
max_dec = get_rep(max_bin,2)
print("max_bin: " + str(max_bin) )
print("max_dec: " + str(max_dec) )

found_coin_jams = [[0,0,0,0,0,0,0,0,0,0] for i in range(J)]

n_jams = 0
for i in range(0,max_dec+1):

    #if(i % 10 == 0):
    #print("We are at: " + str(i))

    if n_jams >= J:
        break;
    current_bin = expand_string(bin(i)[2:],M)
    print(str(n_jams) + " " + str(current_bin))

    c_jam = list(map(int,[1] + list(current_bin) + [1]))
    rep_list = [0 for j in range(10)]
    break_loop = False
    for k in range(2,11):
        rep = get_rep(c_jam, k)
        #print("rep: " + str(rep))
        is_rep_prime = is_prime(rep)
        #print(is_rep_prime)
        if(is_rep_prime[0]):
            break_loop = True
            break
        rep_list[k-2] = is_rep_prime[1]
    if break_loop == True:
        continue
    c_jam = list(map(str,c_jam))
    found_coin_jams[n_jams][0] = ''.join(c_jam)
    for k in range(1,10):
        found_coin_jams[n_jams][k] = rep_list[k-1]
    n_jams = n_jams + 1


f = open("result.csv","w")
f.write("Case #1:\n")

for i in range(len( found_coin_jams )):
    s = ""
    for j in range(len( found_coin_jams[i] )):
        s = s + str(found_coin_jams[i][j]) + " "
    s = s + "\n"
    f.write(s)
f.close()






for i in range(2,11):
    rep =  get_rep([1,0,0,0,1,1],i)
    print( str(rep) + " is prime " + str(is_prime(rep)) )





