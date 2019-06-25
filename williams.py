# Copyright 2019 Jihyung Moon
# 
# This file is part of nlp-williams.
# 
# nlp-williams is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# nlp-williams is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with nlp-williams.  If not, see <http://www.gnu.org/licenses/>

import argparse
import sys

import numpy as np
from scipy import stats


def williams_test(r12, r13, r23, n):
    """The Williams test (Evan J. Williams. 1959. Regression Analysis, volume 14. Wiley, New York, USA)
    
    A test of whether the population correlation r12 equals the population correlation r13.
    Significant: p < 0.05
    
    Arguments:
        r12 (float): correlation between x1, x2
        r13 (float): correlation between x1, x3
        r23 (float): correlation between x2, x3
        n (int): size of the population
        
    Returns:
        t (float): Williams test result
        p (float): p-value of t-dist
    """
    if r12 < r13:
        print('r12 should be larger than r13')
        sys.exit()
    elif n <= 3:
        print('n should be larger than 3')
        sys.exit()
    else:
        K = 1 - r12**2 - r13**2 - r23**2 + 2*r12*r13*r23
        denominator = np.sqrt(2*K*(n-1)/(n-3) + (((r12+r13)**2)/4)*((1-r23)**3))
        numerator = (r12-r13) * np.sqrt((n-1)*(1+r23))
        t = numerator / denominator
        p = 1 - stats.t.cdf(t, df=n-3) # changed to n-3 on 30/11/14
        return t, p


if __name__ == '__main__':
		parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
																		description='''\
A test of whether the population correlation r12 equals the population correlation r13
REQUIREMENT: r12 > r13''')
		parser.add_argument('--r12', type=float, required=True, help='correlation between Human and metric A')
		parser.add_argument('--r13', type=float, required=True, help='correlation between Human and metric B')
		parser.add_argument('--r23', type=float, required=True, help='correlation between metric A and metric B')
		parser.add_argument('--n', type=int, required=True, help='sample size (> 3)')
		args = parser.parse_args()
		t, p = williams_test(args.r12, args.r13, args.r23, args.n)
		print("-----------------------------------------")
		print("Williams Test for Increase in Correlation")
		print("")
		print(f"    r12 correlation( Human, metric A ) : {args.r12}")
		print(f"    r13 correlation( Human, metric B ) : {args.r13}")
		print(f"    r23 correlation( metric A, metric B) : {args.r23}")
		print("")
		print(f"    Sample size: {args.n}")
		print("")
		print(f"P-value: {p}")
		print("-----------------------------------------")
