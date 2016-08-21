def parse(N):
    if N == 0:
        return "INSOMNIA"
    else:
        i = 1
        toDo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        while len(toDo) != 0:
            for letter in str(N*i):
                try:
                    toDo.remove(int(letter))
                except:
                    pass
            i = i + 1
        return str((i-1)*N)

numbers = []

with open("/tmp/input.txt", "r") as f:
    for line in f:
        numbers.append(int(line.strip("\n")))

numbers = numbers[1:]
i = 1
for number in numbers:
    print("Case #"+str(i)+": "+parse(number))
    i = i+1
