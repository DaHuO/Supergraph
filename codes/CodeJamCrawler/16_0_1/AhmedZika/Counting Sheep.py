from sys import argv

script, in_file, out_file = argv
input = open(in_file)
content = input.read().splitlines()
input.close()

test_count = 0
test_cases = []
line_index = 0
results = []

for line in content:
    if(line_index == 0):
        test_count = int(line)
    else:
        test_cases.append(int(line))
        
    line_index += 1
    

for case in test_cases:
    if(case == 0):
        results.append("INSOMNIA")
    else:
        i = 0
        finish = False
        track = [False, False, False, False, False, False, False, False, False, False]
        while(finish == False):
            i += 1
            itr = i * case
            values = list(str(itr))
            for value in values:
                for idx in range(0, 10):
                    if(int(value) == idx):
                        track[idx] = True
                        break
            finish = True
            for statue in track:
                if(statue == False):
                    finish = False
                    break
        results.append(itr)

output = open(out_file, "wb")
for res_idx in range(1,(test_count + 1)):
    output.write("Case #" + str(res_idx) + ": " + str(results[res_idx - 1]) + "\n")
output.close()   
    
    
                