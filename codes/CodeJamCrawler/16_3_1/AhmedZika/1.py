from sys import argv

script, in_file  = argv
out = in_file.split(".")
out_file = out[0] + "_out.txt"
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
        test_cases.append(line)
        
    line_index += 1
 
p = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
l = 0
for i in range(0, len(test_cases)):
    part = []
    if(i % 2 != 0):
        results.append('')
        part = test_cases[i].split(" ")
        total = 0
        major = []
        maj_v = 0
        for j in range(0, len(part)):
            part[j] = int(part[j])
            total += part[j]
            if(maj_v < part[j]):
                maj_v = part[j]
                major = [j]
            elif(maj_v == part[j]):
                major.append(j)
                
        while(total > 0):
            c = 0
            if(len(major) > 1) and (len(major) % 2 != 0) and (maj_v == 1):
                results[l] += p[major[0]] + ' '
                total -= 1
                part[major[0]] -= 1
            else:
                for m in major:
                    if(c > 1):
                        break
                    results[l] += p[m]
                    total -= 1
                    part[m] -= 1
                    c += 1
                results[l] += ' '
                
            maj_v = 0
            for j in range(0, len(part)):
                if(maj_v < part[j]):
                    maj_v = part[j]
                    major = [j]
                elif(maj_v == part[j]):
                    major.append(j)
            
        l += 1   
    else:
        continue
    
res_idx = 0
output = open(out_file, "wb")
for res_idx in range(1,(test_count + 1)):
    output.write("Case #" + str(res_idx) + ": " + str(results[res_idx - 1]) + "\n")
    pass
output.close()   