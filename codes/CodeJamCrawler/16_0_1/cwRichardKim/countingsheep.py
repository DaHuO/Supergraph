num_cases = int(raw_input())

for case_num in range(num_cases):
        n = int(raw_input())
        if n == 0:
                print ("Case #%i: INSOMNIA" % (case_num+1))
        else:
                seen = set([int(i) for i in str(n)])
                count = 1
                while len(seen) < 10:
                        count+=1
                        temp_n = n*count
                        for i in str(temp_n):
                                if int(i) not in seen:
                                        seen.add(int(i))
                print ("Case #%i: %i" % ((case_num+1), count*n))

