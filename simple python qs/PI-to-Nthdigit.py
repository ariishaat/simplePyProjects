'''
Enter a number and have the program generate PI up to that 
many decimal places.
'''

import math

def pi_to_N(n):
    '''
    Generates Pi up to n decimal places
    
    pi_to_N: int -> float
    
    Requires: 15 > n >= 0
    '''
    form = "%."+ str(n) + "f" # creates string format
    pi = math.pi
    
    if n == 0:
        return 3
    else:
        return float(form % pi)


'''
define pi w/o 'math.pi':
   pi1 = 4 * math.atan(1)
   pi2 = math.acos(-1)
'''
