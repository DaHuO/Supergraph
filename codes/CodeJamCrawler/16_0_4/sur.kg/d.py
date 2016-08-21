from sys import *;

tc = int(stdin.readline())
for tn in range(tc):
    (k, c, s) = (int (n) for n in stdin.readline().split());
    res = [];
    digits = [0] * c
    digitv = 0
    while digitv < k:
        digitp = 0
        while digitv < k and digitp < c:
            digits[digitp] = digitv
            digitp += 1
            digitv += 1
        mul = 1
        idx = 0
        for digit in digits:
            idx += mul * digit
            mul *= k
        res.append(idx + 1)
    print ("Case #%d: " % (tn+1), end = '')
    if len(res) > s:
        print ('IMPOSSIBLE')
    else:
        print (*res)

supplementary_perl_program = '''
use warnings;
use strict;

my $k = 3;
my $c = 2;

for (my $cc = 0; $cc < $c; $cc++){
    my $s = '';
    for (my $kk = 0; $kk < $k; $kk++){
        $s .= $kk x $k ** ($c - $cc - 1);
        }
    for (my $kk = 0; $kk < $k**($cc); $kk++){
        print $s;
        }
    print "\n";
    }

for (my $patn = 0; $patn < 1<<$k; $patn++){
    my $pat = '';
    my $gg = 'G' x $k;
    for (my $bn = 0; $bn < $k; $bn++){
        $pat .= $patn & (1 << $bn) ? 'L' : 'G';
        }
    my $res = $pat;
    for (my $cc = 1; $cc < $c; $cc++){
        $res =~ s/G/$gg/g;
        $res =~ s/L/$pat/g;
        }
    print "$res\n";
    }
'''

