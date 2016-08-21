
def count_multiple(number):
    if number == 0:
        return -1
    else:
        final_set = set([])
        counter = 1
        while (len(set) < 10):
            number = number*counter
            T2 = set(map(int, x) for x in str(number))
            counter = counter +1
            final_set = final_set.union(T2)
        # print(number)
        return number

if __name__ == "__main__":
    ip = open("input.txt",'r')
    test_cases = int(ip.readline())
    for i in range(test_cases):
        sol = count_multiple(int(ip.readline()))
        if sol == -1:
            print("Case #"+str(i+1)+": INSOMNIA")
        else:
            print("Case #"+str(i+1)+": "+str(sol))