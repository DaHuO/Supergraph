i = int(input())
for case in range(i):
    start = int(input())
    gezien = set()
    aantal = start
    aantal2 = 0
    k = 0
    boolie = True
    while(len(gezien) != 10 and boolie):
        for letter in str(aantal):
            gezien.add(letter)
        aantal += start
        aantal2 += start
        k += 1
        if k > 2000:
            boolie = False
            aantal2 = "INSOMNIA"
    print("Case #{}: {}".format(case + 1,aantal2))