# https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89

def mouth_size(animal): 
    # code here
    return ('small' if animal.lower() == 'alligator' else 'wide')

def mouth_size2(animal): 
    # code here
    s = 'wide'
    if animal.lower() == 'alligator':
        s = 'small'
        return s
    return s