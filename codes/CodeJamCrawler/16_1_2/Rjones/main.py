def main():
    numberofcases = int(input())
    count = 1
    for x in range(numberofcases):
        Ans = []
        dictionary = {}
        sizeofmatrix = int(input())
        for x in range(2*sizeofmatrix-1):
            temp = input()

            temp = temp.split()

            for each in temp:
                if int(each) in dictionary:
                    dictionary[int(each)] += 1
                else:
                    dictionary[int(each)] = 1

        for each in dictionary.keys():
            if dictionary[each] % 2 != 0:
                Ans.append(each)

        Ans.sort()
        Ans = " ".join(str(tempstr) for tempstr in Ans)
        print("Case #%d: %s" %(count,Ans))
        count += 1

if __name__ == "__main__": main()