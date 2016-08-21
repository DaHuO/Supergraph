
for t in range(int(input())):
    N = int(input())
    if N==0:
        print("Case #"+str(t+1) + ": " +"INSOMNIA")

    else:
        i = 1
        dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 0: 0}
        while 1:
            num = N * i
            end = num
            while num:
                digit = num % 10
                if dic[digit] == 0:
                    dic[digit] = 1
                num //= 10

            flag = "green"
            for j in dic:
                if dic[j] == 0:
                    flag = "red"

            if flag == "green":
                print("Case #"+str(t+1) + ": " + str(end))
                break

            i += 1



