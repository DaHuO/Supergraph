# mdnahid22@gmail.com
# Google Code Jam Qualification Round 2016
# Problem A. Counting Sheep

T = int(input())

if (T>=1 and T<=100):

    case = {}
    for i in range(1, T + 1):
        case[i] = int(input())

    for i in range(1, T + 1):
        n = case[i]
        if (n == 0):
            print("case #" + str(i) + ": INSOMNIA")
            continue
        checklist = "0123456789"
        mylist = ""
        count = 1
        while (set(mylist) != set(checklist)):
            m = str(n * count)
            gen = (x for x in m if x not in mylist)
            z = ''.join(gen)
            mylist = mylist + z
            count += 1
        else:
            print("case #" + str(i) + ":", m)

else:
    print("Test cases out of limit..!")
