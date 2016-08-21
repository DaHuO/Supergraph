fin = open("A-large.in")
fout = open("output.txt", "w")

def write_out(counter, text):
    fout.write("Case #" + counter + ": " + text + "\n")

counter = 0

lines = []
for line in fin:
    lines.append(int(line))
lines = lines[1:]

for number in lines:
    counter += 1
    n=0
    seen = [0,0,0,0,0,0,0,0,0,0]
    if number == 0:
        write_out(str(counter), "INSOMNIA")
    else:
        while 0 in seen:
            n += 1
            thinking = str(number * n)
            for char in thinking:
                seen[int(char)] = 1
        write_out(str(counter), thinking)

fin.close()
fout.close()
