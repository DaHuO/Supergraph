__author__ = 'ivan_pavlov'

with open("in.txt", "r") as f:
    size = next(f)
    out = open("res.txt", "w")
    for index, s in enumerate(map(lambda x: x.strip(), f.readlines())):
        print(index)
        out.write("Case #"+str(index+1)+": ")
        s = s[::-1]
        cnt = 0
        while True:
            min_index = s.find("-")

            if min_index == -1:
                break
            cnt += 1
            last_index = min_index
            for i in range(min_index, len(s)):
                if s[i] != "-":
                    break
                last_index = i
            new_s = s[:min_index] + "+" * (last_index - min_index + 1)
            for i in range(last_index + 1, len(s)):
                if s[i] == '-':
                    new_s += '+'
                else:
                    new_s += '-'
            s = new_s
        out.write(str(cnt) + "\n")

