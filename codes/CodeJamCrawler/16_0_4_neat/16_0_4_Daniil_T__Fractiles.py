# it sounds like a quantum calculation
# basically every transformation is kinda applying OR operator to quantum bits.

for test in range(input()):
    print "Case #%d:" % (test + 1),

    tiles, complexity, students = map(int, raw_input().split())

    tiles_to_see = (tiles + complexity - 1) // complexity

    if tiles_to_see > students:
        print "IMPOSSIBLE"
    else:
        next_tile = 0
        for i in xrange(tiles_to_see):

            index = 1

            for j in xrange(complexity):
                index += tiles ** j * next_tile
                next_tile = (next_tile + 1) % tiles

            print index,

        print