n = int(raw_input())
for i in range(n):
    hm = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    num = int(raw_input())
    if num == 0:
        print("Case #" + str(i+1) + ": INSOMNIA")
        continue
    mult = 1
    while True:
        thisnum = num*mult
        numdig = list(str(thisnum))
        for j in numdig:
            hm[j] = hm[j] + 1
        sleep = True
        for key in hm:
            if hm[key] == 0:
                sleep = False
                break
        if sleep:
            print("Case #" + str(i+1) + ": " + str(thisnum))
            break
        mult = mult + 1
