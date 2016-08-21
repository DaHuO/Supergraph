def count_sheeps(n, list_digits):
    #print ("counting sheeps for: %s" % n)
    if n == 0:
        return "INSOMNIA"
    else:
        i = 1
        while list_digits:
            #print("Iterating for n=" +str(n)+", i="+str(i)+", list_digits=" + str(list_digits))
            current_sheep_count = n*i
            digits = [int(i) for i in str(current_sheep_count)]
            for d in digits:
                if d in list_digits:
                    list_digits.remove(d)

            i +=1
        return current_sheep_count


if __name__ == "__main__":
    x = int(input())

    for i in range(1,x+1):
        for s in input().split(" "):
            n = int(s)

        list_digits = {0,1,2,3,4,5,6,7,8,9}
        sheeps = count_sheeps(n, list_digits)

        print("Case #{}: {}".format(i, sheeps))