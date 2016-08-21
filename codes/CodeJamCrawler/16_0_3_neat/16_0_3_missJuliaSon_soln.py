import sys
from copy import copy

class Problem:
  def __init__(self, istrm=sys.stdin, ostrm=sys.stdout):
    self.istrm = istrm
    self.ostrm = ostrm
    self.pfcache = dict()

  def p_mult(self, a, b=[1, 1]):
    #x3 + 1 = yes factorizable over 1-10
    #x+1 no
    pass

  def is_prime(self, n):
    chki = 2
    while (chki-1)*(chki-1) < n:
      if n % chki == 0:
        self.pfcache[n] = chki
        return False
      chki += 1
    self.pfcache[n] = None
    return True

  def accept_composite(self, n1, n2):
    self.pfcache[n1*n2] = n1

  def get_pf(self, n):
    if n not in self.pfcache:
      self.is_prime(self,n)
    return self.pfcache[n]

  def formula_ok(self, n, N):
    strv = str(n)
    if len(strv) > N:
      return False
    return not bool([ch for ch in strv if ch not in ['0', '1']])

# formula comes in decimal
  def formula_eval(self, formula, radix):
    rv = 0
    image = 1
    for coef in reversed([int(ch) for ch in str(formula)]):
      rv += coef*image
      image *= radix
    return rv

  def get_jamcoin_monoms(self, N=32):
    rl = list()
    for pwr in range(2,N):
      # for radix in range(2,11):
      #   evn = radix**pwr+1
      #   print pwr, radix, evn, self.is_prime(evn)
      jamcoin = all([not self.is_prime(radix**pwr+1) for radix in range(2,11)])
      if jamcoin:
        rl.append(pwr)
    return rl

  def do_all_cases(self, case='large'):
    output = set()
    if case=='large':
      N = 32
      J = 500
    elif case=='small':
      N = 16
      J = 50
    elif case=='toy':
      N = 6
      J = 3
    self.ostrm.write('Case #{}:\n'.format(1))
    monoms = [ 1+10**e for e in self.get_jamcoin_monoms(N) ]
    jamcoin_formulas = dict()
    for m in monoms:
      # print 'monom {}'.format(m)
      min_amp = 10**(N-len(str(m))) + 1
      if min_amp == 2:
        jamcoin_formulas[m] = m
      else:
        base_formula = m * min_amp
        # print base_formula
        mults = []
        mult = 1
        rmf = ''
        while len(str(rmf)) < N:
          mult *= 10
          rmf = m*mult
          if self.formula_ok(base_formula + rmf, N):
            mults.append(mult)

        binwidth = len(mults)
        binmod   = 2**binwidth
        for kernel in range(0,binmod):
          emb_formula = base_formula
          for multi, multv in enumerate(mults):
            if (2**multi) & kernel:
              emb_formula += multv * m
          # print kernel, emb_formula
          if self.formula_ok(emb_formula, N):
            jamcoin_formulas[emb_formula] = m
            if len(list(jamcoin_formulas.keys())) >= J:
              break
    # while len(list(jamcoin_formulas)) < J:
    #   
    #   jamcoin_formulas.add
     
    jamcoins_out = 0
    for jamcoin_formula, sub_formula in jamcoin_formulas.items():
      jamcoin_str = str(jamcoin_formula)
      radices = range(2,11)
      dvsrs = list()
      for radix in radices:
        evald_sub  = self.formula_eval(sub_formula    , radix)
        evald_real = self.formula_eval(jamcoin_formula, radix)
        dvsrs.append(self.pfcache[evald_sub])
        sub_check = evald_sub % dvsrs[-1]
        real_check = evald_real % dvsrs[-1]
        if sub_check or real_check:
          print radix, evald_real, dvsrs[-1], evald_sub % dvsrs[-1], evald_real % dvsrs[-1]
      self.ostrm.write('{} {}\n'.format(jamcoin_str, ' '.join([str(n) for n in dvsrs])))
      jamcoins_out += 1
      if jamcoins_out == J:
        break

def main():
  dut = Problem(sys.stdin, sys.stdout)
  dut.do_all_cases()

if __name__ == '__main__':
  main()
