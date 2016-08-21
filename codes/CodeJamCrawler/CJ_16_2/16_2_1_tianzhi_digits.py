cases = input()

for case in range(int(cases)):

    s = list(input().lower())
    anw = ""
    t = s.count("z")
    #print(s)
    for i in range (t):
        zero = ["z","e","r","o"]
        for x in zero:
            for i in range(len(s)):
                if s[i] == x:
                    del s[i]
                    break
        anw += "0"
    #(anw)
    t = s.count("w")
    for i in range (t):
        zero = ["t","w","o"]
        for x in zero:
            for i in range(len(s)):
                if s[i] == x:
                    del s[i]
                    break

        anw += "2"

    t = s.count("u")
    for i in range (t):
        zero = ["f","o","u","r"]
        for x in zero:
            for i in range(len(s)):
                if s[i] == x:
                    del s[i]
                    break
        anw += "4"

    t = s.count("r")
    for i in range (t):
        zero = ["t","h","r","e","e"]
        for x in zero:
            for i in range(len(s)):
                if s[i] == x:
                    del s[i]
                    break
        anw += "3"
    t = s.count("x")
    for i in range (t):
        zero = ["s","i","x"]
        for x in zero:
            for i in range(len(s)):
                if s[i] == x:
                    del s[i]
                    break
        anw += "6"
    t = s.count("s")
    for i in range (t):
        zero = ["s","e","v","e","n"]
        for x in zero:
            for i in range(len(s)):
                if s[i] == x:
                    del s[i]
                    break
        anw += "7"
    t = s.count("f")
    for i in range (t):
        zero = ["f","i","v","e"]
        for x in zero:
            for i in range(len(s)):
                if s[i] == x:
                    del s[i]
                    break
        anw += "5"
    t = s.count("o")
    for i in range (t):
        zero = ["o","n","e"]
        for x in zero:
            for i in range(len(s)):
                if s[i] == x:
                    del s[i]
                    break
        anw += "1"
    t = s.count("g")
    for i in range (t):
        zero = ["e","i","g","h","t"]
        for x in zero:
            for i in range(len(s)):
                if s[i] == x:
                    del s[i]
                    break
        anw += "8"
    t = s.count("i")
    for i in range (t):
        zero = ["n","i","n","e"]
        for x in zero:
            for i in range(len(s)):
                if s[i] == x:
                    del s[i]
                    break
        anw += "9"
    #print(anw)
    a = sorted(anw)
    #print(a)
    #list(anw).sort(key=lambda x:(not x.islower(), x))
    #print(anw)
    print("Case #" + str(case+1) + ": "+ "".join(a))
