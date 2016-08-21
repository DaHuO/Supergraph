for g in range(int(input())):

    check = "0123456789"
    temp_str = input()

    for h in range(100000):
        temp_int = int(temp_str)
        temp_int = temp_int*(h+1)

        for i in str(temp_int):
            check = check.replace(i, "")

        if(check == ""):
            print("Case #" + str(g+1) + ": " + str(temp_int))
            break
    if(check != ""):
        print("Case #" + str(g+1) + ": " + "INSOMNIA")
