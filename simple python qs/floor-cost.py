'''
Find Cost of Tile to Cover W x L Floor - Calculate the total cost of tile it 
would take to cover a floor plan of width and length, using a cost entered by
the user.
'''
import math

def tileCalc():
    '''
    Calculates the cost for a rectangluar floor plan, given the user input for
    the width and length of the floor, and the cost per square foot
    
    tileCalc: None -> None
    
    '''
    width = input('Enter the width of floor (up to two decimal places):')
    length = input('Enter the length of floor (up to two decimal places):')
    cost = input('Enter the cost per square foot :$')
    w = math.ceil(float(width))
    l = math.ceil(float(length))
    
    print ("The cost to cover this floor plan will be $" + str((w*l)*(float(cost))))
    return None
    
