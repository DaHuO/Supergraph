################################################################################
##
# @file main.py
# @date 2016-04-09
# @author Tiago Lobato Gimenes    (tlgimenes@gmail.com)
#
# @copyright Tiago Lobato Gimenes 2015. All rights reserved.
#
# @section LICENSE
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# @section DESCRIPTION
#
#
#
################################################################################

import numpy as np

################################################################################

N=500
J=31

# Need to define it otherwise algorithm takes forever
max_divisor = 10**6

################################################################################

def to_base( base, n ):

    num = 0;
    times = 0;
    for i in range(1, 51):
        if n % 2 == 1:
            num = num + base ** times;
        
        times = times + 1;
        n = n >> 1;

    return num;

################################################################################

def find_divisor( base, coinjam ):
    jam = to_base( base, coinjam )
    sqr = np.sqrt(float(jam)) + 1
    max = int(sqr) if sqr < max_divisor else int(max_divisor)
    
    for i in range(2, max):
        if jam % i == 0:
            return i;

    return -1;

################################################################################

def naive( N, J ):
    
    print("Case #1:")

    divisors = []

    coinjam = 2**(J)+1
    while N > 0:
        divisors.clear();
        for base in range(2,11):
            divisor = find_divisor( base, coinjam )
            if divisor == -1:
                break;
            else:
                divisors.append(divisor)

        if divisor != -1:
            print(format(coinjam, 'b'), divisors)
            N = N - 1
        coinjam = coinjam + 2;


################################################################################

naive( N, J );

################################################################################
