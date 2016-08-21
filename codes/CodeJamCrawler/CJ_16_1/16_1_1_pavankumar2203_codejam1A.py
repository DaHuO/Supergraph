def run_code():
    t = int(input())

    res = []
    for i in range(t):
        word = input()

        temp = []
        combination = []
        for c in word:
            if not temp:
                temp.append(c)
            else:
                curr = temp
                temp = []
                for w in curr:
                    temp.append(w + c)
                    temp.append(c + w)
        n = len(word)

        res.append((i+1,sorted(temp)[-1]))
    for op in res:
        print("Case #" + str(op[0]) + ": " + str(op[1]))

if __name__ == "__main__":
    run_code()
