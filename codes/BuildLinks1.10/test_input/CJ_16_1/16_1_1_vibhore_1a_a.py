from gcj_io import GcjBase


class LastWord(GcjBase):

    def process_case(self):
        S = self.lines
        NS = S[0]
        for ch in S[1:]:
            if ch >= NS[0]:
                NS = ch + NS
            else:
                NS = NS + ch

        self.print_sol(NS)


LastWord(False, 1)