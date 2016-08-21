def Go_To_Sleep(n):
    seen=[False] * 10
    if(n == 0):
        return "INSOMNIA"
    i = 1
    while(True):
        current = n * i
        for digit in str(current):
            seen[long(digit)] = True;
        if False not in seen:
            return str(current)
        i = i + 1

times = input()

for x in range(times):
    print ("Case #" + str(x+1) + ": " + Go_To_Sleep(long(input())))