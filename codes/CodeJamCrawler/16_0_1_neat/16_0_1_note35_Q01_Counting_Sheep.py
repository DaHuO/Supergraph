
def Count_Sheep(case):
    n = input()
    if n == 0:
        ans = "INSOMNIA"
    else:
        count = 2
        num_list = []
        origin = n
        while True:
            n_str = str(n)
            for i in range(0, len(n_str)):
                num_list.append(n_str[i])
            if len(set(num_list)) == 10:
                ans = n
                break
            n = origin*count
            count = count+1

    print "Case #" + str(case) + ": " + str(ans)



if __name__ == "__main__":
    cases = input()
    for case in range(1,cases+1):
        Count_Sheep(case)
