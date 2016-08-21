def cake_maneuver(cakes):
    return cakes.replace('+','@').replace('-','+').replace('@','-')

def make_cakes_happy(cakes):
    maneuvers = 0

    while '-' in cakes:

        sad_index = cakes.rindex('-')

        cakes = cake_maneuver(cakes[:sad_index+1]) + cakes[sad_index+1:]

        maneuvers = maneuvers + 1

    return maneuvers

cases = int(input())

for case in range(0, cases):
    cakes = raw_input()
    maneuvers = make_cakes_happy(cakes)
    print("Case #{}: {}".format(case + 1, maneuvers))
