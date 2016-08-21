import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', dest='fin', action="store", help="Input file")
parser.add_argument('--output-file', dest='fout', action="store", help="Output file")

args = parser.parse_args()

T = None
line_counter = 0
data = []
seen = []
outputs = []

with open(args.fin) as infile:
    for line in infile:
        line_counter += 1

        if line_counter == 1:
            T = int(line)
            continue

        data.append(int(line))

case_counter = 0

for item in data:
    num = item
    case_counter += 1

    num_string = str(num)
    if (len(num_string) == 1):
        if (num == 0):
            outputs.append("Case #" + str(case_counter) + ": INSOMNIA")
            continue

    i = 1
    while len(seen) < 10:
        num = item * i
        num_string = str(num)
        #print num_string
        for ch in num_string:
            if ch not in seen:
                seen.append(ch)
                #print seen
        i += 1

            
    outputs.append("Case #" + str(case_counter) + ": " + str(num))
    seen = []

with open(args.fout, "w") as output:
    for out in outputs:
        output.write("%s\n" % out)
        print out



    

        
        
        
        
