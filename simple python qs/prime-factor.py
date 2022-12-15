'''
Have the program find prime numbers until the user chooses to stop asking for
the next one.
'''

def findPrime(n):
    '''
    Creates a list of prime numbers (if any) up to and including n

    findPrime: int -> int
    '''
    primeL = []
    for num in range(1, n):
        ifPrime = True
        for i in range(2, num):
            if (num % i) == 0:
                ifPrime = False
        if ifPrime:
            primeL.append(num)
    return primeL

def primeForUser():
    '''
    Takes user input to display findPrime, the program will continue to 
    ask for an input till user chooses to stop
    
    primeForUser: None -> None
    '''
    x = input('Please enter a number or type "stop":')
    if x == 'stop':
        print ('Complete')
        return None
    else:
        num = int(x)
        print (findPrime(num))
        primeForUser()
    
