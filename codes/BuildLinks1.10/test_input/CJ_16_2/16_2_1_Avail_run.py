import sys
from collections import OrderedDict

def main(infile, outfile):
    NUMS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    with open(infile) as inf:
        with open(outfile, 'w') as outf:
            test_case = 1
            case_count = int(inf.readline())
            while test_case <= case_count:
                st = list(inf.readline().replace('\n', ''))
                num =''
                min_num_id = 0
                backup_points = []
                
                while len(st) > 0:
                    can_match = []

                    for n in NUMS[min_num_id:]: # nums min and above
                        all_in = True # all letters in
                        chk = list(st)
                        for l in n: # letter in possible match
                            
                            if l in chk:
                                chk.remove(l)
                            else: # not all letters in, move to next n
                                all_in = False
                                break                                

                        if all_in:
                            can_match.append(n)
                    
                    lcm = len(can_match)

                    if lcm == 0:
                        (min_num_id, st, num) = backup_points.pop()
                        print("BACKING UP TO:", min_num_id, st)
                        continue

                    min_num_id = int(NUMS.index(can_match[0]))

                    if lcm > 1:
                        backup_points.append((NUMS.index(can_match[0])+1, list(st), str(num))) 

                    # Remove stuff
                    nid = NUMS.index(can_match[0])
                    num += str(nid) 
                    for l in NUMS[nid]:
                        st.remove(l)


                if len(st) > 0:
                    print("TOGO", ''.join(st))
                    input()

                # Output
                t = "Case #{}: {}".format(test_case, num)
                print(t)
                outf.write(t)

                if test_case != case_count:
                    outf.write('\n')
                test_case += 1


if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    main(infile, outfile)
