#!/usr/bin/env python3
# -*- coding: utf-8 -*-

NO = "IMPOSSIBLE"

states_to_winner = {}


def gen_state(state):
    # 0 = R
    # 1 = P
    # 2 = S
    new_state = list(state)
    new_state[0] += state[1]
    new_state[1] += state[2]
    new_state[2] += state[0]
    return tuple(new_state)


def solve():
    N, R, P, S = map(int, input().split())
    assert 2 ** N == R + P + S
    state = (R, P, S)
    if state not in states_to_winner:
        return NO

    winner = states_to_winner[state]
    tourney = "RPS"[winner]

    for i in range(N):
        rnd = ""
        for c in tourney:
            if c == "R":
                rnd += "RS"
            elif c == "S":
                rnd += "SP"
            else:
                rnd += "PR"
        tourney = rnd

    assert len(tourney) == 2 ** N

    for i in range(N):
        batch = 2 ** i
        nrnd = ""
        okay = False
        for j in range(0, 2 ** N, 2 * batch):
            A = tourney[j: j + batch]
            B = tourney[j + batch: j + 2 * batch]
            nrnd += min(A, B) + max(A, B)
            okay = True

        if okay:
            tourney = nrnd

    return tourney


def init():
    for i in range(3):
        state = [0, 0, 0]
        state[i] = 1
        state = tuple(state)

        for j in range(12):
            state = gen_state(state)
            states_to_winner[state] = i


def main():
    init()
    T = int(input())
    for t in range(T):
        print("Case #{}: {}".format(t + 1, solve()))


if __name__ == "__main__":
    main()
