import sys
import random

N=32
J=500

print("Case #1:")

old = set([""])

res = 0
while res < J:
    r = ""
    while r in old:
        r = "1" + "".join(random.choice(["0", "1"]) for _ in range(N - 2)) + "1"
    old.add(r)

    proof = []
    for base in range(2, 11):
        n = int(r, base=base)

        p = None
        for div in range(2, 150):
            if n % div == 0:
                proof.append(div)
                break

    if len(proof) == 9:
        res += 1
        print(r, " ".join(map(str, proof)))
               
