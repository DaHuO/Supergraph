def solve(input):
    if input==0:
        return "INSOMNIA"

    N=1
    nb_seen = [False]*10
    while False in nb_seen:
        nb=input*N 
        for c in str(nb):
             nb_seen[int(c)] = True
        N += 1

    return nb




f = open("A-large.in") #Modifier fichier !!!
lines = f.readlines()
f.close()

tests_number = int(lines[0])
i = 1

f = open("output",'w+')
for line in lines[1:]:
    f.write("Case #{}: {}\n".format(i, solve(int(line))))
    i += 1

f.close()
