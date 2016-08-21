
class Gamer:
    def __init__(self, letter, count):
        self.letter = letter
        self.count = count

    def __str__(self):
        return "Gamer({0}, {1})".format(self.letter, self.count)

def fight(la, lb):
    if la == 'R' and lb == 'S': return 'R'
    if la == 'R' and lb == 'P': return 'P'
    if la == 'P' and lb == 'S': return 'S'
    if la == 'P' and lb == 'R': return 'P'
    if la == 'S' and lb == 'P': return 'S'
    if la == 'S' and lb == 'R': return 'R'


def get_letters(depth, letter):
    if (depth == 0): return letter

    if letter == 'R':
        left = get_letters(depth-1, 'R')
        right = get_letters(depth-1, 'S')
    if letter == 'S':
        left = get_letters(depth-1, 'S')
        right = get_letters(depth-1, 'P')
    if letter == 'P':
        left = get_letters(depth-1, 'P')
        right = get_letters(depth-1, 'R')
    if left > right:
        return right + left
    return left + right


T = int(input())

for t in range(T):
    N, R, P, S = list(map(int, input().split()))
    RG = Gamer('R', R)
    PG = Gamer('P', P)
    SG = Gamer('S', S)
    answer = True
    result = ""
    while RG.count + PG.count + SG.count > 1 and answer:
        srt = sorted([RG, PG, SG], key=lambda x: x.count)
        if srt[2].count > srt[0].count + srt[1].count:
            answer = False
            break
        lowersum = srt[0].count + srt[1].count
        lowpairs = abs(srt[2].count - lowersum) / 2
        RG = Gamer(fight(srt[0].letter, srt[1].letter), lowpairs)
        PG = Gamer(fight(srt[0].letter, srt[2].letter), srt[0].count - lowpairs)
        SG = Gamer(fight(srt[1].letter, srt[2].letter), srt[1].count - lowpairs)

    if not answer:
        result = "IMPOSSIBLE"
    else:
        if RG.count > 0: winner = RG
        if PG.count > 0: winner = PG
        if SG.count > 0: winner = SG
        result = get_letters(N, winner.letter)

    print("Case #{0}: {1}".format(t+1, result))
