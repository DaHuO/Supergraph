fin = open('A-large.in.txt', 'r')
fout = open('A-large.out', 'w')
cases = int(fin.readline())
for case in range(cases):
    number = int(fin.readline())
    if number == 0:
        fout.write("Case #{0}: INSOMNIA\n".format(case + 1))
    else:
        counted_number = number
        appeared_string = ""
        while len(appeared_string) < 10:
            string = str(counted_number)
            for char in string:
                if char not in appeared_string:
                    appeared_string += char
            counted_number += number
        fout.write("Case #{0}: {1}\n".format(case + 1, string))
