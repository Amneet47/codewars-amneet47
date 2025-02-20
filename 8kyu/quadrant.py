# https://www.codewars.com/kata/643af0fa9fa6c406b47c5399

def quadrant(x, y):
    # Poveli!
    if x > 0 and y > 0:
        return 1
    elif y > 0 and x < 0:
        return 2
    elif x > 0 and y < 0:
        return 4
    else:
        return 3
    pass