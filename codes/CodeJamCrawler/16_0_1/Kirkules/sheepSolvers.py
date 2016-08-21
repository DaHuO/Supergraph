# Kirk Boyer : 2016 Google Code Jam
# Counting Sheep Problem : Qualifying Round

from math import log
full_digits = set('0123456789')


# Brute Force
class bruteforce:
    def __init__(self, n):
        """Take in a starting number n, compute up to 10^(n+1) steps,
        and record either stopping or 10^(n+1)."""
        self.answer = "INSOMNIA"
        self.n = n
        self.steps = 0
        self.limit = 10**(log(n, 10)+2) if n > 0 else 0
        self.digits = set(str(n))

    def done(self):
        return (self.digits == full_digits) or (self.steps > self.limit)

    def solve(self):
        if self.n == 0:
            return

        while not self.done():
            self.steps += 1
            self.digits = self.digits.union(set(str(self.n*self.steps)))

            # print("n={0}: {1}".format(self.n*self.steps, self.digits))

        if self.digits == full_digits:
            self.answer = self.steps*self.n  # "first" step is mult by 1
