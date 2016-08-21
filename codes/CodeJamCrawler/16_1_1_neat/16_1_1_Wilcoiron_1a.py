count = 1

def main():
    global count
    inp = input()
    temp = inp[0]
    for i in range(1, len(inp)):
        if ord(temp[0]) <= ord(inp[i]):
            temp = inp[i] + temp
        else:
            temp = temp + inp[i]
    print("Case #{}: {}".format(count,temp))
    count += 1

if __name__ == "__main__":
    testcases = int(input())
    for i in range(1, testcases + 1):
        main()
