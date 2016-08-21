with open("C:/Users/Anubhav/Desktop/A-large.in", "r") as filein:
    with open("C:/Users/Anubhav/Desktop/A-large.out", "w") as fileout:
        T = int(filein.readline())

        for i in range(T):
            num_freq = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            s = filein.readline()
            for ch in s:
                if ch == 'Z':
                    num_freq[0]+=1
                elif ch == 'W':
                    num_freq[2]+=1
                elif ch == 'U':
                    num_freq[4]+=1
                elif ch == 'X':
                    num_freq[6]+=1
                elif ch == 'G':
                    num_freq[8]+=1

            s = s.replace('E', 'Q', num_freq[0])
            s = s.replace('R', 'Q', num_freq[0])
            s = s.replace('O', 'Q', num_freq[0])
            s = s.replace('T', 'Q', num_freq[2])
            s = s.replace('O', 'Q', num_freq[2])
            s = s.replace('F', 'Q', num_freq[4])
            s = s.replace('O', 'Q', num_freq[4])
            s = s.replace('R', 'Q', num_freq[4])
            s = s.replace('S', 'Q', num_freq[6])
            s = s.replace('I', 'Q', num_freq[6])
            s = s.replace('E', 'Q', num_freq[8])
            s = s.replace('I', 'Q', num_freq[8])
            s = s.replace('H', 'Q', num_freq[8])
            s = s.replace('T', 'Q', num_freq[8])

            for ch in s:
                if ch == 'O':
                    num_freq[1]+=1
                elif ch == 'H':
                    num_freq[3]+=1
                elif ch == 'F':
                    num_freq[5]+=1
                elif ch == 'S':
                    num_freq[7]+=1

            s = s.replace('I', 'Q', num_freq[5])

            num_freq[9] = s.count('I')

            phonenum = '0'*num_freq[0] + '1'*num_freq[1] + '2'*num_freq[2] + '3'*num_freq[3] + '4'*num_freq[4] + '5'*num_freq[5] + '6'*num_freq[6] + '7'*num_freq[7] + '8'*num_freq[8] + '9'*num_freq[9]

            fileout.write("Case #{}: {}\n".format(i+1, phonenum))
        fileout.close()
    filein.close()
