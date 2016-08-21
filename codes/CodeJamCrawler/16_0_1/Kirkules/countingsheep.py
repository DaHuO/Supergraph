# /usr/bin

# Kirk Boyer : 2016 Google Code Jam
# Counting Sheep Problem : Qualifying Round

import sheepSolvers
import sys
import os.path

if __name__ == "__main__":
    # pick solver based on input
    input_name = sys.argv[2]
    solver_name = sys.argv[1]
    solver = getattr(sheepSolvers, solver_name)

    prefix = os.path.splitext(input_name)[0]
    output_name = prefix + ".out"
    # get input list from file
    with open(input_name, 'r') as f:
        num_cases = int(f.readline())
        cases = [solver(int(line)) for line in f]
        with open(output_name, "w+") as fout:
            for i in range(num_cases):
                cases[i].solve()
                # print("Case #{num}: {ans}".format(num=i, ans=cases[i].answer))
                fout.write("Case #{num}: {ans}\n".format(
                    num=i+1,
                    ans=cases[i].answer))
