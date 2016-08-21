with open("B-small-attempt0.in") as ifp, open("derp.out", "w") as ofp:
    t = int(ifp.readline())
    for i in range(t):
        pancake_line = ifp.readline().strip()
        flips_needed = -1
        last_character = "X"
        for a in pancake_line:
            if a == "\n":
                break
            if a != last_character:
                flips_needed += 1
            last_character = a
        if pancake_line[-1] == "-":
            flips_needed += 1
        ofp.write("Case #{}: {}\n".format(i+1, flips_needed))