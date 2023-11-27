'''
Enter a number and have the program generate the Fibonacci 
sequence to that number or to the Nth number.
'''

import math

goldenR = (1 + math.sqrt(5)) / 2

def fibN(n):
    '''
    Computes the fibonacci number for the Nth number
    
    fibN: int -> int
    
    Requires: n > 0
    '''
    step1 = goldenR**n
    step2 = (1-goldenR)**n
    calculate = (step1 - step2)/ math.sqrt(5)
    
    return int(calculate)

def fibseqlist(n):
    '''
    Creates a list of the fibonnaci sequence up to the nth number
    
    fibseqlist: int -> (listof Int)
    
    Requires: n > 0
    '''
    sequenceL = []
    for i in range(n):
        sequenceL.append(fibN(n))
        n = n-1
        if n == 0:
            sequenceL.append(0)
    sequenceL.reverse()
    return sequenceL

def getFibSeq():
    fs = int(input("Enter a number: "))
    print("Fibonnaci sequence up to " + str(fs) + ":", fibseqlist(fs))

getFibSeq()