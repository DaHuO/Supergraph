try:
    infile = open("A-large.in","r")
    cases = int(infile.readline().rstrip("\n"))
    firstnumbers = infile.readlines()
    infile.close()
    outfile = open("answer.txt","a")

    def binary_search(elements,target):
        high = len(elements)-1
        low = 0
        while high>=low:
            mid = (high+low)//2
            if elements[mid] == target:
                return mid
            elif elements[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return False

    for items in range(cases):
        y = firstnumbers[items].rstrip("\n")
        nextnumber = ""
        if y == "0":
            outfile.write("Case #{}: INSOMNIA\n".format(items+1))
        else:
            numbers = ['0','1','2','3','4','5','6','7','8','9']
            x = 1
            while len(numbers) != 0 :
                nextnumber = str(x * int(y))
                for i in range(len(nextnumber)):
                    position = binary_search(numbers,nextnumber[i])
                    if position is not False:
                        del numbers[position]
                x += 1
            outfile.write("Case #{}: {}\n".format(items+1,nextnumber))

except FileNotFoundError:
    print("Enter correct file name")