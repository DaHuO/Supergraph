if __name__ == "__main__":
    with open("A-large.in", 'r') as inputf:
        outputf=open("A-large.out", 'w')
        line = inputf.readline().rstrip("\n")
        test_num = int(line)

        for i in range(1, test_num + 1):
            line = inputf.readline().rstrip('\n')
            chars = []
            for c in line:
                chars.append(c)
            nums = []
            while 'Z' in chars:
                nums.append('0')
                chars.remove('Z')
                chars.remove('E')
                chars.remove('R')
                chars.remove('O')
            end_zero = len(nums)

            while 'W' in chars:
                nums.append('2')
                chars.remove('T')
                chars.remove('W')
                chars.remove('O')
            end_two = len(nums)

            while 'U' in chars:
                nums.append('4')
                chars.remove('F')
                chars.remove('O')
                chars.remove('U')
                chars.remove('R')
            end_four = len(nums)

            while 'X' in chars:
                nums.append('6')
                chars.remove('S')
                chars.remove('I')
                chars.remove('X')

            while 'F' in chars:
                nums.insert(end_four, '5')
                chars.remove('F')
                chars.remove('I')
                chars.remove('V')
                chars.remove('E')

            while 'V' in chars:
                nums.append('7')
                chars.remove('S')
                chars.remove('E')
                chars.remove('V')
                chars.remove('E')
                chars.remove('N')

            while 'R' in chars:
                nums.insert(end_two, '3')
                chars.remove('T')
                chars.remove('H')
                chars.remove('R')
                chars.remove('E')
                chars.remove('E')

            while 'G' in chars:
                nums.append('8')
                chars.remove('E')
                chars.remove('I')
                chars.remove('G')
                chars.remove('H')
                chars.remove('T')

            while 'I' in chars:
                nums.append('9')
                chars.remove('N')
                chars.remove('I')
                chars.remove('N')
                chars.remove('E')

            one_num = len(chars) // 3
            for j in range(one_num):
                nums.insert(end_zero, '1')

            phone = "".join(nums)
            result = "Case #{0}: {1}".format(i, phone)
            outputf.write(result)

            if i < test_num:
                outputf.write("\n")